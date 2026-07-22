import re

from service_packages.service_logger.logger_provider import logger

CHECKED_TEXT = "The found values are between 15 and 239 or 732"
REGEX_PATTERN = r"\d{2,5}"


def main():
    result = re.findall(REGEX_PATTERN, CHECKED_TEXT)
    logger.info(result)
    logger.info(min(result))
    assert min(result) == "15"


if __name__ == "__main__":
    main()
