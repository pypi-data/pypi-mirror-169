from .bp import *
from .bp.model_api import ModelAPI
from .svc import *
from .dmo import *
from .dto import *

from typing import Optional
from .dto.typedefs import InputTags


def ask(input_tags: InputTags,
        user_question: str) -> Optional[str]:
    """ Route the User Question to the appropriate Model and return the Model Response

    Args:
        input_tags (InputTags): the tags or annotations derived from the user question
        user_question (str): the user question

    Returns:
        Optional[str]: the model result (if any)
    """
    api = ModelAPI()
    d_classification_result = api.classify(input_tags)
    if not d_classification_result or not d_classification_result['text']:
        return None

    model = api.initialize(d_classification_result['text'])
    if not model:
        return None

    d_model_result = api.invoke(input_text=user_question, model=model)
    if not d_model_result or not d_model_result['text']:
        return None

    return d_model_result['text']
