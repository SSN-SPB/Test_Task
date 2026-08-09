from decouple import config

# python -m pip install python-decouple
# decouple is a Python library that helps you manage
# your application's configuration settings in a clean and organized way.
# It allows you to separate configuration from code,
# making it easier to manage different environments
# (e.g., development, testing, production)
# and keep sensitive information (like API keys and passwords)
# out of your source code.



def get_path_list():
    return str(config("PATH")).split(";")


def get_not_exist_config():
    print(config("YYY"))


def check_config():
    test_list = list(get_path_list())
    for x in test_list:
        print(x)
    try:
        get_not_exist_config()
    except Exception as e:
        print(f"Config value {e} is not found")


if __name__ == "__main__":
    check_config()
