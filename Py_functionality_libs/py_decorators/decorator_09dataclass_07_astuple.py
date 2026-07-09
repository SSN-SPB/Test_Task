from dataclasses import astuple, dataclass

from service_packages.service_logger.logger_provider import logger

# dataclass.astuple() returns a tuple of the field values
# of the dataclass instance.
# tuple = astuple(person)
# using tuple(person) is not allowed because the
# dataclass instance is not iterable by default
# it is usefull when you want to convert a dataclass
# instance to a tuple for serialization or other purposes.



@dataclass
class Person:
    name: str
    age: int


person = Person("John", 39)

logger.info(person.name)
logger.info(person.age)
logger.info("Convert person as tuple")

logger.info(f" person type : {type(person)}")
logger.info(f" person: {astuple(person)}")

logger.info("Type is the same:")
logger.info(f" person type : {type(person)}")


logger.info("tuple is not allowed. It gives TypeError:")
try:
    logger.info(f" person type : {tuple(person)}")
except TypeError as te:
    logger.info(te)
