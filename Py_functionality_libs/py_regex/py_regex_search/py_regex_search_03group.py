# re.search by group
import re

from service_packages.service_logger.logger_provider import logger

TEST_PHONE_NUMBER = "123-22-186-11"
SEARCH_PATTERN = r"(\d{3})-(\d{2})-(\d{3})-(\d{2})"


def main():
    checked = re.search(SEARCH_PATTERN, TEST_PHONE_NUMBER)
    for i in range(1, len(checked.groups()) + 1):
        logger.info(checked.group(i))
    logger.info(checked.groups())


if __name__ == "__main__":
    main()
