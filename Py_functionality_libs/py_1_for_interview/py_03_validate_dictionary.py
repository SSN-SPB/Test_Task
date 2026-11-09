users = [
    {"id": 1, "username": "alex", "email": "alex@test.com", "role": "admin"},
    {"id": 2, "username": "john", "email": "john@test.com", "role": "user"},
    {"id": 3, "username": "maria", "email": "maria@test.com", "role": "user"},
    {
        "id": 4,
        "username": "sarah",
        "email": "sarah@test.com",
        "role": "moderator",
    },
    {"id": None, "username": "mike", "email": "mike@test.com", "role": "user"},
    {"id": 9, "username": "", "email": "emma@test.com", "role": "admin"},
    {"id": 7, "username": "david", "email": "davidtest.com", "role": "user"},
]


def parser_response(tested_list: list):
    result_list = []
    result_value = True
    counter = 0
    for x in tested_list:
        if type(x["id"]) != int:
            result_list.append(
                f"record {counter} has not the expected"
                f" id type: int, it has value: ({x['id']})"
                f" and type {type(x['id'])}"
            )
        if type(x["username"]) != str or x["username"] == "":
            result_list.append(
                f"record {counter} has wrong username, "
                f" it has value ({x['username']})"
                f" and type {type(x['username'])}"
            )
        if (
            type(x["email"]) != str
            or x["email"] == ""
            or "@" not in str(x["email"])
        ):
            result_list.append(
                f"record {counter} has wrong email, "
                f" it has value ({x['email']})"
                f" and type {type(x['email'])}"
            )
        # print(type(x["id"]))
        counter += 1
    if len(result_list) > 0:
        result_value = False
    return {"is_valid": result_value, "error_list": result_list}


def main():
    print(parser_response(users))


if __name__ == "__main__":
    main()
