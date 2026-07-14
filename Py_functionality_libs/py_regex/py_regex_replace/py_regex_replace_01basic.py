import re
from service_packages.service_logger.logger_provider import logger

search_text_to_replace = "This is a table. The table is big. The table is in the room."


def main():
    new_text = re.sub(r"table", "chair", search_text_to_replace)
    logger.info(f"Updated text is: '{new_text}'")

    # replace only counted number of times - 2
    new_text2 = re.sub(r"table", "chair", search_text_to_replace, 2)
    logger.info(f"Updated text is: '{new_text2}'")





if __name__ == "__main__":
    main()
