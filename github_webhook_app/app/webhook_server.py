from typing import Any, Callable, Dict, NamedTuple, Type

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse

from github_webhook_app.decorators import github_webhook
from uvicorn import run

NOT_AUTHORIZED = HTTPException(401, "Not authorized.")
NOT_ALLOWED = HTTPException(405, "Method not allowed.")
NOT_FOUND  = lambda item_id="item_id": HTTPException(404, f"Item with {item_id} not found.")

def webhook_app_server(annotated_webhook_cls: Type[Any], /, port: int = 3000, autostart: bool = True) -> Callable | None:
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

    def start():
      run(app=app, host="0.0.0.0", port=port)
    
    if autostart:
      start()
      return None
    
    return start