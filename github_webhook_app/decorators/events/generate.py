from enum import IntEnum
from typing import Any, Dict, Set
import signal
import json
from sys import exit, stdin

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
    def {self.name}(method):
      def wrapper(self, *args, **kwargs):
        if not github_webhook.is_webhook(self):
          raise Exception(f"{{self.__class__.__name__\}} has not been decorated with @github_webhook")
          self.__handlers["{self.name}"] = Handler(method, {self.model}, {json.dumps(self.headers)})
    """

def sig_int_handler(_: int, __: Any) -> None:  # pragma: no cover
    exit(Exit.KeyboardInterrupt)

def __generate_decorator(name: str, definition: Dict[str, Any]):
  pass

def main() -> Exit:
  print("hi")
  signal.signal(signal.SIGINT, sig_int_handler)
  try:
    webhook_dict = json.load(stdin)
    print(__file__)
  except Exception as e:
    print(repr(e))
    return Exit.ERROR
  
  return Exit.OK

if __name__ == "__main__":
  main()