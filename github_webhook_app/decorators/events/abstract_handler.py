from abc import ABCMeta
from typing import Dict, Set, Any, Callable, Type, NamedTuple
from github_webhook_app.decorators import github_webhook

import json

from pydantic import BaseModel
class Handler(NamedTuple):
  event: str
  permitted_headers: Set[str]
  bodyType: Type[BaseModel]
  inst: Type
  method: Callable[[Type, Type[BaseModel], Dict[str, str]], None]

class abstract_webhook_handler(metaclass=ABCMeta):
  def __init__(self, inst: Type, event: str, method: Callable[[Type, Type[BaseModel], Dict[str, str]], None], headers: Set[str], bodyType: Type[BaseModel]) -> None:
    if not github_webhook.is_webhook(inst):
      raise Exception(f"{inst.__class__.__name__} has not been decorated with @github_webhook")
    
    handler = Handler(event=event, permitted_headers=headers, bodyType=bodyType, method=method, inst=inst)
    inst.__handlers[event] = method
    self.__handler = handler
  
  def __call__(self, method: Callable, all_headers: Dict[str, str], body: Any) -> Any:
    newBody = json.loads(json.dumps(body), object_hook=self.__handler.bodyType)
    return method(self.__handler.inst, all_headers, newBody)