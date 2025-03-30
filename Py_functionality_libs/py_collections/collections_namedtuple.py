# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# namedtuple 15:-10
from collections import namedtuple


def main():
    Car = namedtuple('Auto', ['Brand', 'Model', 'year'])
    carOne = Car('Ford', 'Focus', 2019)
    print(carOne.Brand)
    # print(dir(carOne))
    for x in dir(carOne):
        function_list = str(x)
        # print(function_list)
    print(carOne._asdict())
    print(carOne.index(2019))
    print(carOne.year)
    print(carOne.__getitem__(1))
    print(carOne.__hash__())
    print(carOne._replace(Brand='opel'))
    carTwo = carOne._replace(Brand='opel')
    print(carOne._asdict())
    print(carTwo._asdict())


if __name__ == "__main__":
    main()
