from dataclasses import dataclass


@dataclass()
class Ball:
    type: str
    subtype: str
    size: int


def get_basic_size(self):
    return self.size


@dataclass()
class Football(Ball):
    type: str = "game"
    subtype: str = "football"
    size: int = 14

    def get_basic_size(self):
        return self.size + 15


@dataclass()
class Basketball(Ball):
    type: str = "game"
    subtype: str = "basketball"
    size: int = 24

    def get_basic_size(self):
        return self.size + 7


class BallFactory:

    @staticmethod
    def select_ball(type_of_the_game):
        if type_of_the_game == "football":
            return Football()
        elif type_of_the_game == "basketball":
            return Basketball()
        else:
            print("This type is not found")


def main():
    ball_factory = BallFactory()
    soccer_ball = ball_factory.select_ball("football")
    print(soccer_ball.get_basic_size())
    basket_ball = ball_factory.select_ball("basketball")
    print(basket_ball.get_basic_size())


if __name__ == "__main__":
    main()
