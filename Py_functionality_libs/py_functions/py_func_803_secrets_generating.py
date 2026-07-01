# https://docs.python.org/3/library/secrets.html
import string
import secrets

time_string = "%Y_%m_%d_%H_%M_%S_%f"


def main():
    password_format = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(password_format) for i in range(12))
    print(password)
    token_secret = secrets.token_urlsafe(16)
    print(token_secret)


if __name__ == "__main__":
    main()
