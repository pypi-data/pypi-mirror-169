from .classification_schema_kb import d_classification_schema as d_classification_schema
from .models_kb import d_models as d_models
from .praxis_pathology_kb import PraxisPathologyKb as PraxisPathologyKb
from .speech_disorder_kb import SpeechDisorderKb as SpeechDisorderKb
from .typedefs import InputTags as InputTags, ServiceEvent as ServiceEvent

def random_praxis_pathology_question() -> str: ...
def random_speech_disorder_question() -> str: ...
