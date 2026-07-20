import re

from service_packages.service_logger.logger_provider import logger

search_text_to_replace = "Mother loves daughter."


def main():
    new_text = re.sub(
        r"(\w+)\s(\w+)\s(\w+)",
        lambda m: f"{m.group(3).capitalize()} {m.group(2)} {m.group(1).lower()}",
        search_text_to_replace,
    )
    logger.info(f"Updated text is: '{new_text}'")
    assert new_text == "Daughter loves mother."


if __name__ == "__main__":
    main()
