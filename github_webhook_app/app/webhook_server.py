from typing import Any, Callable, Dict, Type

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from github_webhook_app.decorators import github_webhook


def webhook_app_server(annotated_webhook_cls: Type[Any], /, port: int = 3000) -> None:
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

    cfg = uvicorn.Config(app=app, host="0.0.0.0", port=port)
    uvicorn.run(cfg)
      