import json
from pathlib import Path
from pydantic import BaseModel
from typing import Optional, List, TypedDict, ForwardRef, TypeVar

SchemaObject = ForwardRef('SchemaObject')

class SchemaObject(BaseModel):
  "$ref": Optional[str]
  type: Optional[str]
  enum: Optional[List[str]]
  required: Optional[List[str]]
  properties: Optional[TypedDict[str, SchemaObject]]

class XGithub(BaseModel):
  "supported-webhook-types": List[str]

class WebhookRequestBody(BaseModel):
  required: bool
  content: TypedDict[str, SchemaObject]

class WebhookMethodDefinition(BaseModel):
  requestBody: WebhookRequestBody

class WebhookDefinition(BaseModel):
  post: WebhookMethodDefinition

class Webhooks(TypedDict[str, WebhookDefinition]):
  pass

class Components(TypedDict[str, SchemaObject]):
  pass

T = TypeVar('T')
def load_schema_file(path: str, returnType: T) -> T:
  with open(path, "r") as fp:
    return json.load(fp, object_hook=returnType)
  
def load_webhooks(path: str) -> Webhooks:
  return load_schema_file(Path(path, "webhooks.json"), Webhooks)

def load_components(path: str) -> Components:
  return load_schema_file(Path(path, "components.json"), Components)