#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# type: ignore
""" Invoke the Named Model using a provided Callback """


from typing import Any
from typing import Optional
from typing import Callable

from baseblock import BaseObject

from speech_patho_mdl.dto import ServiceEvent


class InvokeNamedModel(BaseObject):
    """Invoke the Named Model using a provided Callback"""

    def __init__(self) -> None:
        """Change Log

        Created:
            26-Sept-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                model: Callable,
                input: Optional[Any],
                source_user: Optional[str],
                target_user: Optional[str]) -> ServiceEvent:
        """Invoke the callable Model object

        Args:
            model (Callable): a callback to an intialized model
            input (object, optional): an untyped input - could be text, list, dictionary - etc
                if no input is provided, the model will be invoked without input
            source_user (str): the source user responsible for the input text
                if no source_user is provided, the model will be invoked without source_user
            target_user (str): the user to whom the text is addressed
                if no target_user is provided, the model will be invoked without target_user

        Returns:
            dict or None: a service result (if any)
        """

        if not model:
            self.logger.error("No Initialized Model Provided")
            raise ValueError

        if input and source_user and target_user:
            return model(
                input_text=input,
                source_user=source_user,
                target_user=target_user,
            )

        if input:
            return model(input)

        return model()
