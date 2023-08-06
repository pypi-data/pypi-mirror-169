#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# type: ignore
""" Handle a Request for a Pathology Question """


import os

from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import ServiceEventGenerator

from openai_helper import OpenAICustomModel
from speech_patho_mdl.dto.typedefs import ServiceEvent


class CustomOpenAIPathology(BaseObject):
    """Handle a Request for a Pathology Question"""

    def __init__(self, d_config: dict):
        """ Change Log

        Created:
            20-Apr-2022
            craig@bast.ai
            *   https://github.com/grafflr/graffl-core/issues/303
        Updated:
            2-May-2022
            craig@bast.ai
            *   renamed from 'handle-speech-disorder-question'
                https://github.com/grafflr/graffl-core/issues/333
        Updated:
            13-Aug-2022
            craig@bast.ai
            *   refactor return types
                https://bast-ai.atlassian.net/browse/COR-94
        Updated:
            26-Sept-2022
            craigtrim@gmail.com
            *   migrated to 'speech-patho-mdl'

        Args:
            d_config (dict): configuration dictionary for models
        """
        BaseObject.__init__(self, __name__)
        self._d_config = d_config
        self._generate_event = ServiceEventGenerator().process

        self._query = OpenAICustomModel(
            model_name=d_config["openai"]["model_name"]).process

    def process(self,
                input_text: str) -> ServiceEvent:

        sw = Stopwatch()
        output_events = []

        if self.isEnabledForDebug:
            Enforcer.is_str(input_text)

        # Expected Format:
        # Answer a Pathology Question: <Question>
        input_text = input_text.split(":")[-1].strip()

        # query_results, query_event
        d_query_result = self._query(input_text)
        [output_events.append(x) for x in d_query_result["events"]]

        if not d_query_result["text"]:
            return {
                "text": None,
                "events": output_events
            }

        output_answer = d_query_result["text"][0]
        output_context = d_query_result["text"][1]

        if self.isEnabledForDebug:
            Enforcer.is_str(output_answer)
            Enforcer.is_str(output_context)

        output_text = f"_{output_answer}_\n\n {output_context}"

        # COR-80; Generate an Event Record
        output_events.append(
            self._generate_event(
                service_name=self.component_name(),
                event_name=os.environ["MODEL_HANDLER_EVENT"],
                stopwatch=sw,
                data={
                    "input_text": input_text,
                    "output_answer": output_answer,
                    "output_context": output_context,
                    "output_text": output_text,
                    "config": self._d_config,
                },
            )
        )

        return {
            "text": output_text,
            "events": output_events
        }
