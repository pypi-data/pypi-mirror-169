from baseblock import BaseObject
from speech_patho_mdl.dto import ServiceEvent as ServiceEvent
from typing import Any, Callable, Optional

class InvokeNamedModel(BaseObject):
    def __init__(self) -> None: ...
    def process(self, model: Callable, input: Optional[Any], source_user: Optional[str], target_user: Optional[str]) -> ServiceEvent: ...
