import json
import signal
from enum import IntEnum
from os.path import dirname
from pathlib import Path
from sys import exit, stdin, argv
from typing import Any, Callable, Dict, List, Set
from datetime import datetime
from datamodel_code_generator import generate, InputFileType
from datamodel_code_generator.format import PythonVersion
import traceback

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
  def handle_{to_snake_case(self.name)}(self, func):
    return self._wrap(func, event_name="{self.name}", request_body=github_webhook_app.models.{self.model})
"""

def sig_int_handler(_: int, __: Any) -> None:  # pragma: no cover
  exit(Exit.KeyboardInterrupt)

def to_camel_case(kebab_str: str) -> str:
  return "".join(x.capitalize() for x in kebab_str.lower().split("-"))

def to_snake_case(kebab_str: str) -> str:
  return kebab_str.replace("-", "_")

def file(subpath: str) -> Path:
  return Path(dirname(__file__), subpath)

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

def generate_decorators() -> Exit:
  handlers: Set[WebhookEventDecorator] = set()
  handler_names: Set[str] = set()
  try:
    webhook_dict = json.loads(stdin.read())["x-webhooks"]
    for name, defn in webhook_dict.items():
      decorator_definition = __generate_decorator(name, defn)
      if decorator_definition is not None:
        handlers.add(decorator_definition)
        handler_names.add(f"handle_{to_snake_case(name)}")
  except Exception as e:
    raise e
  
  comment = f"""
# Webhook event decorators
#   DO NOT EDIT
#   Generated on {datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")}Z

"""
  
  class_base = ""
  with open(file("templates/webhook.py.tmpl"), "r") as template:
    class_base = template.read()

  with open(file("github_webhook_app/__init__.py"), "wt+") as initpy:
    lines = [comment, class_base]
    sorted_handlers = sorted(handlers, key=lambda x: x.name)
    for h in sorted_handlers:
      lines.append(str(h))
    
    lines.append('\nname = "github_webhook_app"\n')
    initpy.writelines(lines)

  return Exit.OK

def generate_models() -> Exit:
  input = stdin.read()
  generate(input,
           input_file_type=InputFileType.OpenAPI,
           output=file("github_webhook_app/models/__init__.py"),
           target_python_version=PythonVersion.PY_311,
           use_annotated=True, field_constraints=True, use_generic_container_types=True,
           use_double_quotes=True, use_union_operator=True,
           use_unique_items_as_set=True, use_field_description=True,
           use_schema_description=True, collapse_root_models=True,
           force_optional_for_required_fields=True)
  
  return Exit.OK

def usage(force: bool = False):
  if force or len(argv) != 2:
    print(f"{argv[0]} models | decorators")
    exit(255)

def main() -> Exit:
  signal.signal(signal.SIGINT, sig_int_handler)

  usage()
  gtype = argv[1]

  f: Callable | None = None
  if gtype == "models":
    f = generate_models
  elif gtype == "decorators":
    f = generate_decorators
  
  if f is None:
    usage(True)

  try:
    return f()
  except KeyboardInterrupt:
    return Exit.KeyboardInterrupt
  except Exception:
    print(traceback.format_exc())
    return Exit.ERROR
  

if __name__ == "__main__":
  exit(main())