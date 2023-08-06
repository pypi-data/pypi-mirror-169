#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# type: ignore
""" Classify the Incoming Tags (annotations) and find a corresponding Model Query (if any) """


import os
from typing import List
from typing import Optional


from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import ServiceEventGenerator

from schema_classification import SchemaOrchestrator

from speech_patho_mdl.dto import InputTags
from speech_patho_mdl.dto import ServiceEvent
from speech_patho_mdl.dto import d_classification_schema


class ClassifyInputTags(BaseObject):
    """Classify the Incoming Tags (annotations) and find a corresponding Model Query (if any)"""

    def __init__(self) -> None:
        """Change Log

        Created:
            26-Sept-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)
        self._generate_event = ServiceEventGenerator().process
        self._classify = SchemaOrchestrator(d_classification_schema).run

    @staticmethod
    def _extract_result(d_classify: dict) -> Optional[str]:
        if not d_classify or not len(d_classify):
            return None
        if ("result" not in d_classify or d_classify["result"] is None or not len(d_classify["result"])):
            return None

        top_result = d_classify["result"][0]["confidence"]
        if top_result >= 80:
            return d_classify["result"][0]["classification"]

        return None

    def process(self,
                input_tags: InputTags) -> ServiceEvent:

        sw = Stopwatch()
        output_events: List = []

        d_classify = self._classify(input_tags)

        classification = self._extract_result(d_classify)
        if not classification:
            return {
                "text": None,
                "events": output_events
            }

        # COR-80; Generate an Event Record
        output_events.append(
            self._generate_event(
                service_name=self.component_name(),
                event_name=os.environ["CORE_EVENT"],
                stopwatch=sw,
                data={
                    "input_tags": input_tags,
                    "d_output": d_classify,
                    "classification": classification,
                }))

        return {
            "text": classification,
            "events": output_events
        }
