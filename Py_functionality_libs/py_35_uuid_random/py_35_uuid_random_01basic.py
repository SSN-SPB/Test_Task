from uuid import uuid4


def main():
    my_uuid1 = uuid4()
    my_uuid3 = str(uuid4())[0:8]
    print("Your UUID is: " + str(my_uuid1))
    print("Your UUID1 is: " + my_uuid3)


if __name__ == "__main__":
    main()
