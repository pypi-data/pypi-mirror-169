from _typeshed import Incomplete as Incomplete
from typing import Any, Dict, List, Optional, TypedDict

class ServiceEvent(TypedDict):
    text: Optional[str]
    events: List[Dict[str, Any]]

InputTags: Incomplete
