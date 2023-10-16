import json
import signal
from enum import IntEnum
from os.path import dirname
from pathlib import Path
from sys import exit, stdin
from typing import Any, Dict, List, Set
from datetime import datetime

class Exit(IntEnum):
    """Exit reasons."""

    OK = 0
    ERROR = 1
    KeyboardInterrupt = 2

class WebhookEventDecorator:
  def __init__(self, name: str, passed_headers: Set[str], model_name: str) -> None:
    self._name = name
    self._passed_headers = passed_headers
    self._model_name = model_name
  
  @property
  def name(self):
    return self._name

  @property
  def headers(self):
    return self._passed_headers
  
  @property
  def model(self):
    return self._model_name

  def __str__(self) -> str:
    return f"""
class handle_{to_snake_case(self.name)}(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("{self.name}", {str(self.headers).replace("'", '"')}, github_webhook_app.models.{self.model})
"""

def sig_int_handler(_: int, __: Any) -> None:  # pragma: no cover
  exit(Exit.KeyboardInterrupt)

def to_camel_case(kebab_str: str) -> str:
  return "".join(x.capitalize() for x in kebab_str.lower().split("-"))

def to_snake_case(kebab_str: str) -> str:
  return kebab_str.replace("-", "_")

def __generate_decorator(name: str, definition: Dict[str, Any]) -> WebhookEventDecorator | None:
  headers: Set[str] = set()
  if "post" not in definition:
    return None
  
  definition = definition["post"]
  if "x-github" in definition:
    xg: Dict[str, Any] = definition["x-github"]
    if "supported-webhook-types" in xg:
      stypes: List[str] = xg["supported-webhook-types"]
      if "repository" in stypes:
        if "parameters" in definition:
          params: List[Any] = definition["parameters"]
          for param in params:
            if "in" in param and param["in"] == "header":
              headers.add(param["name"])
      else:
        return None  
    else:
      return None
  else:
    return None
  
  if "requestBody" in definition:
    if "content" in definition["requestBody"]:
      if "application/json" in definition["requestBody"]["content"]:
        schema = definition["requestBody"]["content"]["application/json"]["schema"]
        if "$ref" in schema:
          bodyTypeSegments = str(schema["$ref"]).split("/")
          bodyType = bodyTypeSegments[len(bodyTypeSegments) - 1]
          return WebhookEventDecorator(name, headers, to_camel_case(bodyType))
  
  return None

def main() -> Exit:
  signal.signal(signal.SIGINT, sig_int_handler)

  handlers: Set[WebhookEventDecorator] = set()
  try:
    webhook_dict = json.load(stdin)
    for name, defn in webhook_dict.items():
      decorator_definition = __generate_decorator(name, defn)
      if decorator_definition is not None:
        handlers.add(decorator_definition)
  except Exception as e:
    raise e
  
  with open(Path(dirname(__file__), "__generated.py"), "wt+") as fp:
    fp.write(f"""
# Webhook event decorators
# DO NOT EDIT
# Generated on {datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")}Z

import github_webhook_app.models
from .abstract_handler import abstract_webhook_handler

              """)
    
    for h in handlers:
      fp.write(str(h))

  return Exit.OK

if __name__ == "__main__":
  main()