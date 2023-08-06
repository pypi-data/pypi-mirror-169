from .bp import *
from .svc import *
from .dmo import *
from .dto import *
from .dto.typedefs import InputTags
from typing import Optional

def ask(input_tags: InputTags, user_question: str) -> Optional[str]: ...
