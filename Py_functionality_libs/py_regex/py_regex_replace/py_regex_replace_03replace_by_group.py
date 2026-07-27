import re

from service_packages.service_logger.logger_provider import logger
text_to_replace = "Mother loves daughter."


def main():
    new_text = re.sub(r"(\w+)\s(\w+)\s(\w+)", r"\3 \2 \1", text_to_replace)
    logger.info(f"Updated text is: '{new_text}'")
    assert new_text == "daughter loves Mother."


if __name__ == "__main__":
    main()
