import inspect
from typing import Callable, Dict


class github_webhook:
  __is_github_webhook_cls: bool = False
  __handlers: Dict[str, Callable] = dict()

  def __init__(self):
    pass

  def __call__(self, cls):
    if cls is None:
      raise "Cannot decorate None"
    
    resolved = None
    if inspect.isclass(cls):
      resolved = cls
    elif hasattr(cls, "__class__"):
      resolved = cls.__class__
    
    if resolved is None:
      raise "argument is not a class or an instance of a class"
    
    resolved.__is_github_webhook_cls = True
    return cls

  @classmethod
  def is_webhook(self, arg) -> bool:
    return hasattr(arg, "__is_github_webhook_cls") and arg.__is_github_webhook_cls
