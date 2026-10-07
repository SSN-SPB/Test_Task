import logging

import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

test_text = [
    "Hello",
    "Привет",
    "España",
    "日本語",
    "😀",
]


@pytest.mark.parametrize("text", test_text)
def test_encode(text):
    encoded_text = text.encode("utf-8")
    logger.info(encoded_text)
    decoded_text = encoded_text.decode("utf-8")
    logger.info(decoded_text)
    assert text == decoded_text
