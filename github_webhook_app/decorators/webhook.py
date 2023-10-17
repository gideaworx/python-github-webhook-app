import inspect
from typing import Dict
from .events import EventHandler

class github_webhook:
  def __init__(self, cls):
    if cls is None:
      raise "Cannot decorate None"
    
    resolved = None
    if inspect.isclass(cls):
      resolved = cls
    elif hasattr(cls, "__class__"):
      resolved = cls.__class__

    resolved._is_github_webhook_cls = True
    resolved._handlers: Dict[str, EventHandler] = dict()
    
    if resolved is None:
      raise "argument is not a class or an instance of a class"
    
    def fget(name: str) -> EventHandler | None:
      if name in resolved._handlers:
        return resolved._handlers[name]
      
      return None

    def fset(name: str, handler: EventHandler) -> None:
      resolved._handlers[name] = handler

    resolved.handler = property(
      fget=fget, 
      fset=fset,
      fdel=None,
      doc="registered event handlers for the decorated class",
    )

  def __call__(self, cls):
    return cls

  @classmethod
  def is_webhook(self, arg) -> bool:
    return hasattr(arg, "_is_github_webhook_cls") and arg._is_github_webhook_cls
