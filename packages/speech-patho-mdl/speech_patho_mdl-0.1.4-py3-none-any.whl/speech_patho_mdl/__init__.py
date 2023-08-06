from .dto.typedefs import InputTags
from typing import Optional
from .dto import *
from .dmo import *
from .svc import *
from .bp.model_api import ModelAPI
from .bp import *
import os
os.environ["MODEL_HANDLER_EVENT"] = "speech-patho-mdl"


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
