import logging
from dataclasses import dataclass

"""The @dataclass decorator, available in the dataclasses module,
simplifies the creation of classes by automatically generating common methods
 such as __init__, __repr__, and __eq__"""


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s\t%(levelname)s\t%(filename)s:%(lineno)d\t%(message)s",
)
logger = logging.getLogger(__name__)


# without decorator @dataclass
class Park:

    def __init__(self, city, park_name, park_size):
        self.city = city
        self.park_name = park_name
        self.park_size = park_size

    def __repr__(self) -> str:
        return f"Park attribute(city = {self.city}, park_name = {self.park_name}, park_size = {self.park_size})"

    def __eq__(self, other):
        if isinstance(other, Park):
            return (
                other.park_size == self.park_size
                and other.park_name == self.park_name
                and other.city == self.city
            )
        return False


park_one = Park("SPB", "Letniy", 20)
park_three = Park("SPB", "Letniy", 20)
park_two = Park("MSC", "Alexandrovsky", 10)

logger.info(park_one == park_two)
logger.info(park_one == park_three)
logger.info(park_three)


@dataclass(order=True)  # order=True добавляет методы сравнения
class Park2:
    city: str
    park_name: str
    park_size: int

    def __repr__(self) -> str:
        return f"Park2 attribute(city = {self.city}, park_name = {self.park_name}, park_size = {self.park_size})"

    def __eq__(self, other):
        if isinstance(other, Park2):
            return (
                other.park_size == self.park_size
                and other.park_name == self.park_name
                and other.city == self.city
            )
        return False


park_one = Park2("SPB", "Letniy", 20)
park_three = Park2("SPB", "Letniy", 20)
park_two = Park2("MSC", "Alexandrovsky", 10)

logger.info(park_one == park_two)
logger.info(park_one == park_three)
logger.info(park_three)
logger.info(park_two)
park_two.city = "Volgograd"
logger.info(park_two)
