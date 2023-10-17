import inspect
import uvicorn

from abc import ABCMeta
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from typing import Any, Callable, Dict, NamedTuple, Set, Type, TypeVar
from pydantic import BaseModel

class EventHandler(NamedTuple):
  event: str
  bodyType: Type[BaseModel]
  method: Callable

WEBHOOK_HEADERS = {"X-Hub-Signature-256", 
                   "User-Agent", 
                   "X-Github-Hook-Id", 
                   "X-Github-Hook-Installation-Target-Id", 
                   "X-Github-Hook-Installation-Target-Type", 
                   "X-Github-Event", 
                   "X-GitHub-Delivery"}

T = TypeVar('T', bound=BaseModel)

class ABCWebhookService(metaclass=ABCMeta):
  @staticmethod
  def is_webhook(arg) -> bool:
    return hasattr(arg, "_is_github_webhook_cls") and arg._is_github_webhook_cls

  def __init__(self):
    app = FastAPI()
    self._app = app
    self._handlers: Dict[str, EventHandler] = dict()


    @app.post("/event")
    async def handleEvent(request: Request) -> Any:
      json = await request.json()

      if "X-Github-Event" not in request.headers:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Not Found"})
      event = request.headers["X-Github-Event"].replace("_", "-")
      
      if "action" not in json:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Not Found"})
      action = json["action"]

      handler_type = f"{event}-{action}"
      handler = self._handlers[handler_type]

      if handler is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Not Found"})
      
      event_headers: Dict[str, str] = dict()
      for header_name in WEBHOOK_HEADERS:
        if header_name in request.headers:
          event_headers[header_name] = request.headers[header_name]
      
      return handler.method(headers=event_headers, request=handler.bodyType(**json))

  def webhook(self, cls):
    if cls is None:
      raise "Cannot decorate None"
    
    resolved = None
    if inspect.isclass(cls):
      resolved = cls
    elif hasattr(cls, "__class__"):
      resolved = cls.__class__

    resolved._is_github_webhook_cls = True
    self._target = cls
  

  def _wrap(self, func, /, event_name: str, request_body: T) -> Callable:
    self._handlers[event_name] = EventHandler(event=event_name, bodyType=request_body, method=func)
    def wrapped(inst, /, headers: Dict[str, str], request: T):
      return func(inst, headers, request)

    return wrapped

  def start(self, port: int = 3000):
    uvicorn.run(self._app, host="0.0.0.0", port=port)
