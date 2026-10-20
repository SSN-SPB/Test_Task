class SelectedCarSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._initialised = False
        return cls._instance

    def __init__(self, speed):
        if not self._initialised:
            self.speed = speed
            self._initialised = True

    def get_speed(self):
        return self.speed


def main():
    car_one = SelectedCarSingleton(15)
    car_two = SelectedCarSingleton(18)
    print(f"if car1 is car2: {car_two is car_one}")
    print(car_one.get_speed())
    print(car_two.get_speed())
    assert car_two is car_one
    assert car_two.get_speed() == car_one.get_speed()
    assert car_two.get_speed() == 15


if __name__ == "__main__":
    main()
