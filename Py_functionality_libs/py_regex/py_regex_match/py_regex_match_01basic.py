import re

from service_packages.service_logger.logger_provider import logger

email_text_to_check = "john.smith@test.com"
# email_text_to_check = "john.2smith@test.com" not valid

test_pattern = r"\D+\.\D+\@\D+\.\w+"


def main():
    if re.match(test_pattern, email_text_to_check):
        logger.info("Email is valid")
    else:
        logger.info("Email is not valid")


if __name__ == "__main__":
    main()
