#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# type: ignore
""" Load the Model Config """


from typing import Dict
from typing import List

from baseblock import BaseObject

from speech_patho_mdl.dto import d_models


class ModelConfigLoader(BaseObject):
    """Load the Model Config"""

    def __init__(self) -> None:
        """Change Log

        Created:
            26-Sept-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)
        self._models = d_models["models"]

    def by_name(self,
                model_name: str) -> Dict:
        """Find Model configuration by Name

        Args:
            model_name (str): Model Name

        Raises:
            ValueError: Model Name Not Found

        Returns:
            dict: the Model configuration
        """

        for model in self._models:
            if model["name"] == model_name:
                return model

        self.logger.error("\n".join([
            "Model Not Found",
            f"\tModel Name: {model_name}"]))

        raise ValueError

    def all(self) -> List:
        """Return all Model Configurations

        Returns:
            list: all model configurations
        """
        return self._models
