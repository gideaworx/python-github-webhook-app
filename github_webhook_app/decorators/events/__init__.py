from .abstract_handler import *

class EventHandler(NamedTuple):
  event: str
  permitted_headers: Set[str]
  bodyType: Type[BaseModel]
  inst: Type
  method: Callable