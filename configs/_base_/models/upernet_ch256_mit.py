# ---------------------------------------------------------------
# Copyright (c) 2022-2024 Yc.Zhang, Zx.Wang. All rights reserved.
# Licensed under the Apache License, Version 2.0
# ---------------------------------------------------------------

_base_ = ['upernet_mit.py']

model = dict(decode_head=dict(channels=256, ))
