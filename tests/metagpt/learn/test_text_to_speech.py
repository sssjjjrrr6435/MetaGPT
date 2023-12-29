#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/8/18
@Author  : mashenquan
@File    : test_text_to_speech.py
@Desc    : Unit tests.
"""

import pytest

from metagpt.config import CONFIG
from metagpt.learn.text_to_speech import text_to_speech


@pytest.mark.asyncio
async def test_text_to_speech():
    # Prerequisites
    assert CONFIG.IFLYTEK_APP_ID
    assert CONFIG.IFLYTEK_API_KEY
    assert CONFIG.IFLYTEK_API_SECRET
    assert CONFIG.AZURE_TTS_SUBSCRIPTION_KEY and CONFIG.AZURE_TTS_SUBSCRIPTION_KEY != "YOUR_API_KEY"
    assert CONFIG.AZURE_TTS_REGION

    # test azure
    data = await text_to_speech("panda emoji")
    assert "base64" in data or "http" in data

    # test iflytek
    key = CONFIG.AZURE_TTS_SUBSCRIPTION_KEY
    CONFIG.AZURE_TTS_SUBSCRIPTION_KEY = ""
    try:
        data = await text_to_speech("panda emoji")
        assert "base64" in data or "http" in data
    finally:
        CONFIG.AZURE_TTS_SUBSCRIPTION_KEY = key


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
