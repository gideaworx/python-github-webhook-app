import inspect
import sys

from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi_class import View
from github_webhook_app.decorators import github_webhook
from typing import Type, Any, NamedTuple, Callable, Dict

NOT_AUTHORIZED = HTTPException(401, "Not authorized.")
NOT_ALLOWED = HTTPException(405, "Method not allowed.")
NOT_FOUND  = lambda item_id="item_id": HTTPException(404, f"Item with {item_id} not found.")

class ServerControls(NamedTuple):
  start: Callable | None
  stop: Callable | None

def webhook_app_server(annotated_webhook_cls: Type[Any], /, port: int = 3000, autostart: bool = True):
  if not github_webhook.is_webhook(annotated_webhook_cls):
    raise TypeError(f"{repr(annotated_webhook_cls)} must be a class decorated with @github_webhook")

  app = FastAPI()

  @app.post("/event")
  async def handlePost(request: Request):
    json = await request.json()

    if "X-Github-Event" not in request.headers:
      return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Not Found"})
    event = request.headers["X-Github-Event"]
    
    if "action" not in json:
      return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Not Found"})
    action = json["action"]

    handler_type = f"{event}-{action}"
    handler = annotated_webhook_cls.handler(handler_type)

    if handler is None:
      return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Not Found"})
    
    event_headers: Dict[str, str] = dict()
    for header_name in handler.permitted_headers:
      if header_name in request.headers:
        event_headers[header_name] = request.headers[header_name]
    
    handler.method(handler.inst, headers=event_headers, request=json)

app = FastAPI()

@View(app, path="/event")
class EventHandler:
  exceptions = {
    "__all__": [NOT_FOUND],
    "post": [NOT_ALLOWED, NOT_FOUND]
  }

  RESPONSE_CLASS = {
    "post": PlainTextResponse
  }

  def post(self):
    pass

class GithubWebhookApp:
  def __init__(self, webhook_cls = None) -> None:
    self.app = FastAPI()
    
    if webhook_cls is None:
      webhooks = inspect.getmembers(sys.modules[__name__], github_webhook.is_webhook)
      if len(webhooks) == 1:
        webhook_cls = webhooks[0][1]
      else:
        raise f"If webhook_cls is not passed, there must be exactly one defined webhook in the loaded modules, but I found {len(webhooks)}"
    
    self.__webhook = webhook_cls
    if inspect.isclass(webhook_cls):
      self.__webhook = webhook_cls()