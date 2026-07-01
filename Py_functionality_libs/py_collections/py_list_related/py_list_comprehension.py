import logging

test_list = [10, 12, -7, 11, -7, 14, 15, 10, 12, -7, 11, 10, -7, 12, 11, 10]
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s\t%(levelname)s\t%(filename)s:%(lineno)d\t%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",  # Define the date format
)


def main():
    list_comprehension_even = [n for n in test_list if n % 2 == 0]
    logger.info(f"The filtered list: {list_comprehension_even}")


if __name__ == "__main__":
    main()
