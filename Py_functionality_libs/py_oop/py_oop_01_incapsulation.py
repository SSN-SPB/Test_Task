import logging
import random

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)


class TestSuite:
    """Suite demonstrates oop Python"""
    test_counter = 0

    def __init__(self, name):
        # self.result = None
        self.name = name

    def get_test_name(self):
        return self.name

    def set_test_result(self, result):
        self.result = result

    def is_attribute_available(self):
        if hasattr(self, 'result'):
            return True
        else:
            return False

    @classmethod
    def get_test_counter(cls):
        """@classmethod can be called without creating object of class"""
        return cls.test_counter

    @staticmethod
    def get_random_value():
        return random.sample(range(11, 99), 15)


def main():
    ts = TestSuite("tdk")
    logger.info(TestSuite.get_test_counter())
    logger.info(ts.get_test_counter())
    logger.info(TestSuite.get_random_value())
    logger.info(ts.get_random_value())
    logger.info(ts.is_attribute_available())
    ts.set_test_result("good")
    logger.info(ts.is_attribute_available())
    logger.info(ts.get_random_value())


if __name__ == "__main__":
    main()

