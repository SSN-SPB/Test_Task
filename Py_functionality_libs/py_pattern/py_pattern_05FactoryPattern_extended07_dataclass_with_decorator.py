from dataclasses import dataclass
from abc import abstractmethod, ABC


@dataclass
class Games(ABC):
    type: str
    duration: int

    @abstractmethod
    def get_duration(self):
        return self.duration


@dataclass
class Soccer(Games):
    type: str = "outside game"
    duration: int = 90
    name: str = "soccer"
    additional_duration: int = 10

    def get_duration(self):
        return self.duration + self.additional_duration


@dataclass
class Volley(Games):
    type: str = "outside game"
    duration: int = 90
    name: str = "volleyball"
    additional_duration: int = 10

    def get_duration(self):
        return self.duration + self.additional_duration

    def get_name(self):
        return self.name


class FactoryGame:
    @staticmethod
    def selected_game(game_name):
        if game_name == "football":
            return Soccer()
        if game_name == "Volley":
            return Volley()


def adding_header(func):

    def wrapper(text):
        print(text)
        return func()

    return wrapper


@adding_header
def selecting_game():
    factory = FactoryGame()

    first_game = factory.selected_game("football")
    second_game = factory.selected_game("Volley")

    print(first_game.get_duration())
    print(second_game.get_name())
    print(second_game.additional_duration)


if __name__ == "__main__":
    selecting_game("start selecting game")
