from dataclasses import dataclass, field
import logging

# the field init=False is used to indicate that
# the salary_after_tax attribute should not be included
# in the generated __init__ method.
# This means that when creating an instance of
# the Employee class, you only need to provide
# values for the title and salary attributes,
# and the salary_after_tax attribute will
# be automatically calculated based on
# the provided salary value.


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s\t%(levelname)s\t%(filename)s:%(lineno)d\t%(message)s",
)
logger = logging.getLogger(__name__)


@dataclass
class Employee:
    title: str
    salary: float
    salary_after_tax: float = field(init=False)

    def __post_init__(self):
        self.salary_after_tax = self.salary * 0.8


employee1 = Employee("Engineer", 50000)


logger.info(employee1.title)
logger.info(employee1.salary_after_tax)
