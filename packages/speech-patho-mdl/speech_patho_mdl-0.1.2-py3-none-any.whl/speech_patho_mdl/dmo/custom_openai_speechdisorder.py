#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# type: ignore
""" Handle a Request for a Speech Disorder Question """


import os

from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import TextUtils
from baseblock import ServiceEventGenerator

from openai_helper import OpenAICustomModel
from speech_patho_mdl.dto.typedefs import ServiceEvent


class CustomOpenAISpeechDisorder(BaseObject):
    """Handle a Request for a Speech Disorder Question"""

    def __init__(self, d_config: dict):
        """ Change Log

        Created:
            25-Apr-2022
            craig@bast.ai
            *   https://github.com/grafflr/graffl-core/issues/298
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
        # Answer a Speech Disorder Question: <Question>
        input_text = input_text.split(":")[-1].strip()

        # query_results, query_event
        d_query_result = self._query(input_text)
        [output_events.append(x) for x in d_query_result["events"]]

        # query_results == "*** OPENAI DISABLED ***":
        if not d_query_result["text"]:
            return {
                "text": None,
                "events": output_events
            }

        output_answer = d_query_result["text"]
        output_context = d_query_result["text"]

        if self.isEnabledForDebug:
            Enforcer.is_str(d_query_result["text"])
            Enforcer.is_str(d_query_result["text"])

        def combined_text() -> str:
            if TextUtils.jaccard_similarity(output_answer, output_context) > 0.90:
                return output_answer
            return f"_{output_answer}_\n\n {output_context}"

        output_text = combined_text()

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
