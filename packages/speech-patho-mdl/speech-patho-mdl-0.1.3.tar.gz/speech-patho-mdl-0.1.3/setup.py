# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['speech_patho_mdl',
 'speech_patho_mdl.bp',
 'speech_patho_mdl.dmo',
 'speech_patho_mdl.dto',
 'speech_patho_mdl.svc']

package_data = \
{'': ['*']}

install_requires = \
['baseblock',
 'boto3',
 'openai-helper',
 'openai>=0.20.0,<0.21.0',
 'opensearch-helper',
 'opensearch-py>=1.1.0,<2.0.0',
 'owl-builder',
 'owl-parser',
 'requests',
 'schema-classification']

setup_kwargs = {
    'name': 'speech-patho-mdl',
    'version': '0.1.3',
    'description': 'Custom Trained Models for Speech Pathology',
    'long_description': '# Speech Pathology Models (speech-patho-mdl)\nCustom Speech Pathology Models\n\n\n# Quick-and-Dirty\n```python\nfrom speech_pathology_model import ask\n\n# On-Topic Question\nanswer = ask("How is velopharyngeal function typically evaluated?")\nassert answer == "Velopharyngeal function during speech may also be evaluated by the measurement of pressure and airflow."\n\n# Off-Topic Question\nanswer = ask("How\'s the Weather??")\nassert not answer\n```\nThe system will only return answers for on-topic questions within the scope of the knowledge base.  No chit-chat or "cute" responses will be provided for off-topic or out-of-domain questions.  This is the declared responsibility of the consumer.\n\n# Detailed Usage\n\n## Initialize API\n```python\napi = ModelAPI()\n```\n\n## Input\nA list of tags (annotations), likely derived from unstructured text using an NLP or analytics engine\n```python\ninput_tags: List[str] = []\n```\n\n## Classify Tags\n```python\nd_result = api.classify(input_tags)\nclassification = d_result[\'text\']\n```\nThis will return a type of `typedefs.dto.ServiceEvent`:\n```python\nclass ServiceEvent(TypedDict):\n    text: Optional[str]\n    events: List[Dict[str, Any]]\n```\n\nThe `text` attribute of this output object will be either `None` or have a value.\n\nIf the value is `None`, this means no relevant speech pathology classification was found.\n\nIf a string value does exist, this will be the top result.\n\nThe system defines the top result as\n1. Having the maximum confidence level in a list of results\n2. Having a confidence of at least 80%\n\n## Initialize and Invoke a Model\nIn the event of a classification being returned:\n```python\nmodel = api.initialize(classification)\nd_result = api.invoke(model, "How is velopharyngeal function typically evaluated?")\n```\nThis result is also of type `typedefs.dto.ServiceEvent` and the model answer can be retrieved as\n```python\nanswer = d_result[\'text\']\nassert answer == "Velopharyngeal function during speech may also be evaluated by the measurement of pressure and airflow."\n```',
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': 'Craig Trim',
    'maintainer_email': 'craigtrim@gmail.com',
    'url': 'https://github.com/craigtrim/speech-patho-mdl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
