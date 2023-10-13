import inspect
import sys

from fastapi import FastAPI, APIRouter, HTTPException, status
from fastapi.responses import PlainTextResponse
from fastapi_class import View
from github_webhook_app.decorators import GithubWebhook

NOT_AUTHORIZED = HTTPException(401, "Not authorized.")
NOT_ALLOWED = HTTPException(405, "Method not allowed.")
NOT_FOUND  = lambda item_id="item_id": HTTPException(404, f"Item with {item_id} not found.")

app = FastAPI()

@View(app, path="/handle")
class Handler:
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
      webhooks = inspect.getmembers(sys.modules[__name__], GithubWebhook.is_webhook)
      if len(webhooks) == 1:
        webhook_cls = webhooks[0][1]
      else:
        raise f"If webhook_cls is not passed, there must be exactly one defined webhook in the loaded modules, but I found {len(webhooks)}"
    
    self.__webhook = webhook_cls
    if inspect.isclass(webhook_cls):
      self.__webhook = webhook_cls()