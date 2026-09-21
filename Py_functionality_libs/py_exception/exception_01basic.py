def main():
    list = [0, 1]
    list.append("x")
    print(list)  # [0, 1, 'x']
    try:
        list.append("y", "z")
    except Exception as e:
        print(e)
        print(e.__dict__)
        print(dir(e))


if __name__ == "__main__":
    main()
