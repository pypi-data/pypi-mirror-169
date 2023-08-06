#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# type: ignore
""" Handle a Request for a Random Pathology Question """


import os

from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import ServiceEventGenerator

from speech_patho_mdl.dto.typedefs import ServiceEvent
from speech_patho_mdl.dto import random_praxis_pathology_question


class RandomPathologyQuestion(BaseObject):
    """Handle a Request for a Random Pathology Question"""

    def __init__(self) -> None:
        """Change Log

        Created:
            20-Apr-2022
            craigtrim@gmail.com
            *   https://github.com/grafflr/graffl-core/issues/303
        Updated:
            25-Apr-2022
            craigtrim@gmail.com
            *   determine when to repeat the prompt back to the source user
                https://github.com/grafflr/graffl-core/issues/308
        Updated:
            5-Aug-2022
            craigtrim@gmail.com
            *   remove the 'input-text' parameter; why was this needed? in pursuit of
                https://bast-ai.atlassian.net/browse/COR-63
        Updated:
            13-Aug-2022
            craigtrim@gmail.com
            *   refactor return types
                https://bast-ai.atlassian.net/browse/COR-94
        Updated:
            26-Sept-2022
            craigtrim@gmail.com
            *   migrated to 'speech-patho-mdl'
        """
        BaseObject.__init__(self, __name__)
        self._generate_event = ServiceEventGenerator().process

    def process(self) -> ServiceEvent:

        sw = Stopwatch()
        output_events = []

        random_question = random_praxis_pathology_question()
        if self.isEnabledForDebug:
            Enforcer.is_str(random_question)

        output_text = f"answer a speech pathology question: {random_question}"

        # COR-80; Generate an Event Record
        output_events.append(
            self._generate_event(
                service_name=self.component_name(),
                event_name=os.environ["MODEL_HANDLER_EVENT"],
                stopwatch=sw,
                data={
                    "input_text": None,
                    "output_text": output_text,
                },
            )
        )

        return {
            "text": output_text,
            "events": output_events
        }
