#!/usr/bin/env python
# -*- coding: UTF-8 -*-


__model_hints = [
    'pathology',
    'speech pathology',
    'praxis'
]

model_hints = [
    x.strip().lower()
    for x in sorted(__model_hints, key=len)
]
