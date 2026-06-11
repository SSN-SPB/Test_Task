# https://docs.python.org/3/library/logging.html

# %(filename)s	Filename only (myscript.py)
# %(pathname)s	Full path to the source file
# %(lineno)d	Source line number
# %(funcName)s	Function name
# %(name)s	Logger name
# %(levelname)s	Log level (INFO, ERROR, etc.)
# %(asctime)s	Timestamp
# %(threadName)s	Thread name

import logging

logger = logging.getLogger(__name__)
# to see in pytest log: pytest -v --log-cli-level=INFO


logging.basicConfig(
    # Set minimal level of logging
    # All level are available starting with DEBUG
    # available levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    # level=logging.DEBUG,  # Set log level DEBUG
    # Available ERROR, CRITICAL starting with ERROR
    # level=logging.ERROR,  # Set the log level ERROR
    # level INFO - all messages with level INFO and higher will be logged
    level=logging.INFO,
    # Set required format if not default:
    # Define the log format
    # format='%(asctime)s - %(levelname)s - %(message)s',
    # format="%(asctime)s - %(levelname)s-%(filename)s:%(lineno)d-%(message)s",
    format="%(asctime)s\t%(levelname)s\t%(filename)s:%(lineno)d\t%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",  # Define the date format
)


def do_something():
    print("print")
    logger.debug("Doing something debug")
    logger.error("Doing something error")
    logger.info("Doing something")
    logger.critical("Doing something critical")


def main():
    do_something()


if __name__ == "__main__":
    main()
