# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# type: ignore
""" Generic Facade to interact with Speech Disorder Data """


from random import sample

from baseblock import BaseObject


class SpeechDisorderKb(BaseObject):
    """Generic Facade to interact with Speech Disorder Data"""

    __questions = [
        'What are some common oral mechanism examination findings in UUMN dysarthria?',
        'What are some examples of how categorizing dysarthrias into types can be helpful?',
        'What are some of the abnormalities that could reflect functional differences between the two vocal folds?',
        'What are some of the benefits of speech therapy?',
        'What are some of the characteristics of UMN dysarthria?',
        'What are some of the other characteristics of UUMN dysarthria?',
        'What are some of the phonatory abnormalities in people with UUMN dysarthria?',
        'What are some of the primary clinical speech characteristics of UUMN dysarthria?',
        'What are some of the symptoms of hypernasality?',
        "What are some other patients' characteristics?",
        'What are some possible causes of dysphonia in people with UUMN lesions?',
        'What are some possible explanations for dysarthria?',
        'What are the characteristics of dysarthria?',
        'What are the findings of reduced force and endurance generally supportive of?',
        'What are the implications of a mixed spastic-hypokinetic dysarthria for motor speech disorders?',
        'What are the questions that arise when the lesion is in the presumed dominant hemisphere?',
        'What are the results of the acoustic and physiologic studies of patients with UUMN dysarthria?',
        'What are the symptoms of UUMN dysarthria?',
        'What are the symptoms of a middle cerebral artery stroke?',
        'What are the symptoms of dysarthria?',
        'What are the symptoms of motor neuron disease?',
        'What are the three capsular/putaminal aphasia syndromes?',
        'What are the two types of UMN dysarthria?',
        'What are the various consequences of subcortical?',
        'What can laryngeal dysfunction lead to?',
        'What is Aronson AE typically able to do?',
        'What is Attig E typically able to do?',
        'What is UMN dysarthria?',
        'What is UUMN dysarthria?',
        'What is a confident clinical diagnosis of any dysarthria type?',
        'What is a mixed dysarthria?',
        'What is a specific diagnosis?',
        'What is ataxic hemiparesis?',
        'What is dysarthria?',
        'What is frontal lobe ataxia?',
        'What is hypernasality?',
        'What is laryngeal function?',
        'What is pure dysarthria?',
        'What is the Diadochokinetic syllable rate?',
        'What is the anatomic designation of this dysarthria type based on?',
        'What is the association of dysarthria with apparent ataxia and dysmetria?',
        'What is the cause of motor neuron disease?',
        'What is the difference between dysarthria and apraxia of speech?',
        'What is the effect of acute hemiplegia on intercostal muscle activity?',
        'What is the evidence of aphasia in this case?',
        'What is the evidence that at least some patients have weakness of the articulators contralateral to the side of lesion?',
        'What is the internal capsule?',
        'What is the most common deviant speech characteristic of those with UUMN dysarthria?',
        'What is the most common reason for low confidence in the diagnosis of UUMN?',
        'What is the most common type of dysarthria?',
        'What is the most frequent designation for UUMN?',
        'What is the most important time to use these qualified diagnostic conclusions?',
        'What is the most likely cause of UUMN dysarthria in this case?',
        'What is the reason for AMRs in UUMN dysarthria?',
        'What is the side and somatotopical location of single small infarcts in the corona radiata and pontine base in relation to contralateral limb paresis and dysarthria?',
        'What is the value of categorizing dysarthrias into types?',
        'Why is a diagnosis of UUMN dysarthria not always possible on the basis of speech features alone?'
    ]

    def __init__(self) -> None:
        """Change Log

        Created:
            25-Apr-2022
            craig@bast.ai
            *   in pursuit of
                https://github.com/grafflr/graffl-core/issues/298
        Updated:
            28-Apr-2022
            craig@bast.ai
            *   migrated to the modelquery microservice in pursuit of
                https://github.com/grafflr/graffl-core/issues/405
        Updated:
            4-Aug-2022
            craig@bast.ai
            *   retrieve files from S3
                also renamed from 'find-speech-disorder' to befit 'dto' pkg status
                https://bast-ai.atlassian.net/browse/COR-53
        Updated:
            26-Sept-2022
            craigtrim@gmail.com
            *   migrated to 'speech-patho-mdl'
        """
        BaseObject.__init__(self, __name__)

    def random(self) -> str:
        return str(sample(self.__questions, 1)[0])
