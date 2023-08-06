# Speech Pathology Models (speech-patho-mdl)
Custom Speech Pathology Models


# Quick-and-Dirty
```python
from speech_pathology_model import ask

# On-Topic Question
answer = ask("How is velopharyngeal function typically evaluated?")
assert answer == "Velopharyngeal function during speech may also be evaluated by the measurement of pressure and airflow."

# Off-Topic Question
answer = ask("How's the Weather??")
assert not answer
```
The system will only return answers for on-topic questions within the scope of the knowledge base.  No chit-chat or "cute" responses will be provided for off-topic or out-of-domain questions.  This is the declared responsibility of the consumer.

# Detailed Usage

## Initialize API
```python
api = ModelAPI()
```

## Input
A list of tags (annotations), likely derived from unstructured text using an NLP or analytics engine
```python
input_tags: List[str] = []
```

## Classify Tags
```python
d_result = api.classify(input_tags)
classification = d_result['text']
```
This will return a type of `typedefs.dto.ServiceEvent`:
```python
class ServiceEvent(TypedDict):
    text: Optional[str]
    events: List[Dict[str, Any]]
```

The `text` attribute of this output object will be either `None` or have a value.

If the value is `None`, this means no relevant speech pathology classification was found.

If a string value does exist, this will be the top result.

The system defines the top result as
1. Having the maximum confidence level in a list of results
2. Having a confidence of at least 80%

## Initialize and Invoke a Model
In the event of a classification being returned:
```python
model = api.initialize(classification)
d_result = api.invoke(model, "How is velopharyngeal function typically evaluated?")
```
This result is also of type `typedefs.dto.ServiceEvent` and the model answer can be retrieved as
```python
answer = d_result['text']
assert answer == "Velopharyngeal function during speech may also be evaluated by the measurement of pressure and airflow."
```