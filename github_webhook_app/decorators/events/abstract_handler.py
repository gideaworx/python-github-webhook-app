from abc import ABCMeta
from typing import Dict, Set, Any, Callable, Type, NamedTuple
from github_webhook_app.decorators import github_webhook
from pydantic import BaseModel
from . import EventHandler

class abstract_webhook_handler(metaclass=ABCMeta):
  def __init__(self, method: Callable) -> None:
    if not hasattr(method, "__self__"):
      raise Exception(f"{self.__class__.__name__} only works on class methods")
    
    inst = method.__self__
    self._inst = inst
    self._method = method
    if not github_webhook.is_webhook(inst):
      raise Exception(f"{inst.__class__.__name__} has not been decorated with @github_webhook")

  def _set_targets(self, event: str, headers: Set[str], bodyType: Type[BaseModel]) -> None:
    handler = EventHandler(event=event, permitted_headers=headers, bodyType=bodyType, method=self._method, inst=self._inst)
    self._inst.handler(event, handler)
    self._handler = handler

  def __call__(self, _: Callable, /, headers: Dict[str, str], request: Any) -> Any:
    newBody = self._handler.bodyType(**request)
    return self._method(self._handler.inst, headers=headers, request=newBody)