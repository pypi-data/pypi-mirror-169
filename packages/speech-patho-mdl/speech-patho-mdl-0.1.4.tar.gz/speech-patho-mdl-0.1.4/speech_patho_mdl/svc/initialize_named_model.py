#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# type: ignore
""" Find and Initialize the Model Query """


from baseblock import BaseObject

from speech_patho_mdl.dmo import ModelConfigLoader


class InitializeNamedModel(BaseObject):
    """Find and Initialize the Model Query"""

    def __init__(self) -> None:
        """Change Log

        Created:
            26-Sept-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)
        self._model_finder = ModelConfigLoader().by_name

    def process(self,
                classification: str) -> object or None:
        """Initialize the Model for the incoming Classification

        Args:
            classification (str): the classification outcome from a prior step

        Raises:
            NotImplementedError: no model exists for this classification

        Returns:
            object or None: the initialized model (if any)
        """

        if not classification or not len(classification):
            return None

        if "#" in classification:
            classification = classification.split("#")[0].strip()

        if classification == "RandomSpeechPathology":
            from speech_patho_mdl.dmo import RandomPathologyQuestion

            return RandomPathologyQuestion().process

        if classification == "RandomSpeechDisorder":
            from speech_patho_mdl.dmo import RandomSpeechDisorderQuestion

            return RandomSpeechDisorderQuestion().process

        if classification == "SearchSpeechPathology":
            from speech_patho_mdl.dmo import CustomOpenAIPathology

            return CustomOpenAIPathology(d_config=self._model_finder("SearchSpeechPathology")).process

        if classification == "SearchSpeechDisorder":
            from speech_patho_mdl.dmo import CustomOpenAISpeechDisorder

            return CustomOpenAISpeechDisorder(d_config=self._model_finder("SearchSpeechDisorder")).process

        raise NotImplementedError(classification)
