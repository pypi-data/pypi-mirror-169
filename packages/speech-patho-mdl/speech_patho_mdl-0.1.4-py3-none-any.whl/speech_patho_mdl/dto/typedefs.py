#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from typing import Any
from typing import AnyStr
from typing import List
from typing import Dict
from typing import Tuple
from typing import TypedDict
from typing import NewType
from typing import Union
from typing import Optional


class ServiceEvent(TypedDict):
    text: Optional[str]
    events: List[Dict[str, Any]]


InputTags = NewType("InputTags", List[str])
