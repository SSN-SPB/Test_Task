import inspect

from service_packages.service_logger.logger_provider import logger

# inspect.getgeneratorstate() we can check the state of a generator


def to_inspect():
    yield "Hello"
    yield "World"
    yield "again"


def main():
    gen = to_inspect()
    logger.info(inspect.getgeneratorstate(gen))
    logger.info(next(gen))
    logger.info(inspect.getgeneratorstate(gen))
    logger.info(next(gen))
    logger.info(inspect.getgeneratorstate(gen))
    list(gen)
    logger.info(inspect.getgeneratorstate(gen))
    try:
        next(gen)
        logger.info(inspect.getgeneratorstate(gen))
    except StopIteration as si:
        logger.info(si.__traceback__)
        print("StopInteration error")


if __name__ == "__main__":
    main()
