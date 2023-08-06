from .typedefs import InputTags
from .typedefs import ServiceEvent
from .models_kb import d_models
from .classification_schema_kb import d_classification_schema
from .praxis_pathology_kb import PraxisPathologyKb
from .speech_disorder_kb import SpeechDisorderKb
from .model_type_hints_kb import model_hints


_praxis_kb = PraxisPathologyKb()
_speech_kb = SpeechDisorderKb()


def random_praxis_pathology_question() -> str:
    return _praxis_kb.random()


def random_speech_disorder_question() -> str:
    return _speech_kb.random()
