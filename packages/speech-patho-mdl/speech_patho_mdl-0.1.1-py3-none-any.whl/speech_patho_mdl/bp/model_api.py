#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# type: ignore
""" Speech Pathology Model API """


from typing import Optional
from typing import Callable

from baseblock import Enforcer
from baseblock import BaseObject
from speech_patho_mdl.dto import ServiceEvent

from speech_patho_mdl.svc import ClassifyInputTags
from speech_patho_mdl.svc import InvokeNamedModel
from speech_patho_mdl.svc import InitializeNamedModel


class ModelAPI(BaseObject):
    """ Speech Pathology Model API """

    def __init__(self) -> None:
        """Change Log

        Created:
            26-Sept-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)
        self._invoke_model = InvokeNamedModel().process
        self._initialize_model = InitializeNamedModel().process
        self._classify_tags = ClassifyInputTags().process

    def classify(self,
                 input: list) -> ServiceEvent:
        """Determine if a model exists for the given annotations

        Args:
            input (list or str): either a list of annotations or plain input text
                e.g.,   as a list,  the input might be ['nursing', 'masters_degree', 'mba']

        Returns:
            str or None: a classification result (if any)
        """
        _type = type(input)
        if _type == list:
            d_result = self._classify_tags(input)

            # Guarantee the return type contract
            if self.isEnabledForDebug and d_result:
                Enforcer.keys(d_result, "events", "text")

            return d_result

        raise NotImplementedError(_type)

    def initialize(self,
                   classification: str) -> Optional[Callable]:
        """Initialize the correct Model based on the Classification

        Args:
            classification (str): the model recipe to invoke

        Returns:
            Callable or None: the instantiated model (if any)
        """

        return self._initialize_model(classification)

    def invoke(self,
               model: Callable,
               input_text: Optional[str],
               source_user: Optional[str],
               target_user: Optional[str]) -> ServiceEvent:
        """Query Model based on the Classification Recipe

        Args:
            model (Callable): the model recipe to invoke
            input_text (str): any input text of any length
                if no input_text is provided, the model will be invoked without input_text
            source_user (str): the source user responsible for the input text
                if no source_user is provided, the model will be invoked without source_user
            target_user (str): the user to whom the text is addressed
                if no target_user is provided, the model will be invoked without target_user

        Returns:
            dict or None: the result
        """

        d_result = self._invoke_model(
            model=model,
            input=input_text,
            source_user=source_user,
            target_user=target_user,
        )

        # Guarantee the return type contract
        if self.isEnabledForDebug:
            Enforcer.keys(d_result, "events", "text")

        return d_result
