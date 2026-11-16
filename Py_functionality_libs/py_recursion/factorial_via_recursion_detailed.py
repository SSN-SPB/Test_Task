import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def factorial(counter):
    if counter == 0:
        return 1
    logger.info("counter is {}".format(counter))
    logger.info(
        "interim result is {}".format(counter * factorial(counter - 1))
    )
    return counter * factorial(counter - 1)


def main():
    logger.info(factorial(5))
    # logger.info(factorial(1))


if __name__ == "__main__":
    main()
