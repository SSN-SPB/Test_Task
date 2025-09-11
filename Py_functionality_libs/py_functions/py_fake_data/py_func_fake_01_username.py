from faker import Faker


fake = Faker()


def main():
    username = fake.user_name()
    password = fake.password(length=12, special_chars=True)
    print(username)
    print(password)
    assert len(password) == 12


if __name__ == "__main__":
    main()

#
# Output:
# Expression(
#     body=BinOp(
#         left=Name(id='a', ctx=Load()),
#         op=Add(),
#         right=BinOp(
#             left=Name(id='b', ctx=Load()),
#             op=Mult(),
#             right=Constant(value=2))))
