import pytest
from uuid import uuid4
import logging

logger = logging.getLogger(__name__)


@pytest.fixture()
def fixture_factory():
    def create_user():
        return {
            "user_name": "John",
            "user_email": f"John_{uuid4()}@test.com",
        }

    return create_user


def test_two_users(fixture_factory):
    user_one = fixture_factory()
    user_two = fixture_factory()
    logger.info(user_one)
    assert user_one != user_two
