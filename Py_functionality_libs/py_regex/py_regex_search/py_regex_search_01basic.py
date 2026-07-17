import re

from service_packages.service_logger.logger_provider import logger

CHECKED_PATTERN = r"\d-\d{2}-\d{2}-\d{2}"

tested_text = "This is a phone 2-12-85-06 I remember ever"


def main():
    search_result = re.search(CHECKED_PATTERN, tested_text)
    if search_result:
        logger.info("Required is found.")
    else:
        logger.info("Required is not found.")


if __name__ == "__main__":
    main()
