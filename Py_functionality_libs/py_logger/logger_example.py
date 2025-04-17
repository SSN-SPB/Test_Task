# https://docs.python.org/3/library/logging.html

import logging

logger = logging.getLogger(__name__)
# to see in pytest log: pytest -v --log-cli-level=INFO


logging.basicConfig(
    # Set minimal level of logging
    # All level are available starting with DEBUG
    # available levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    # level=logging.DEBUG,  # Set log level DEBUG
    # Available ERROR, CRITICAL starting with ERROR
    level=logging.ERROR,  # Set the log level ERROR
    # Set required format if not default:
    # Define the log format
    # format='%(asctime)s - %(levelname)s - %(message)s',
    # datefmt='%Y-%m-%d %H:%M:%S'  # Define the date format
)


def do_something():
    print("print")
    logger.debug("Doing something debug")
    logger.info("Doing something")
    logger.critical("Doing something critical")


def main():
    do_something()


if __name__ == "__main__":
    main()
