from flashtext import KeywordProcessor
from service_packages.service_logger.logger_provider import logger

TARGET_TEXT = "The Java and Python"

kb = KeywordProcessor()


def check_flash():
    logger.info("Test flashtext")
    kb.add_keyword("Java", "Python")
    return kb.replace_keywords(TARGET_TEXT)


def main():
    logger.info(check_flash())


if __name__ == "__main__":
    main()
