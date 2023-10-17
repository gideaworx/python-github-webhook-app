from .abstract_handler import *
from .__generated import *

class EventHandler(NamedTuple):
  event: str
  permitted_headers: Set[str]
  bodyType: Type[BaseModel]
  inst: Type
  method: Callable