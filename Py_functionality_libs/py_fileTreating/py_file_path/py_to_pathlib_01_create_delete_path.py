import logging
import random
from pathlib import Path

random_values = [random.randint(12, 10000) for _ in range(10)]
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def creating_file_with_random_values(initial_list):
    logger.info("Creating file with random values...")
    logger.info(initial_list)
    with open("output.txt", "w") as file:
        for value in initial_list:
            file.write(f"Value for {initial_list.index(value)} is {value}\n")

    logger.info("File created with random values.")


def deleting_file_by_name(file_name):
    Path(file_name).unlink()
    logger.info(f"Deleted file {Path(file_name)}")


def main():
    # Write value to file
    creating_file_with_random_values(random_values)
    # Deleting file by name
    deleting_file_by_name("output.txt")


if __name__ == "__main__":
    main()
