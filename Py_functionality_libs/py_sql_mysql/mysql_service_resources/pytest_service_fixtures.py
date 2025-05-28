import pytest


from mysql_service_resources import (
    check_if_schema_exists,
    get_list_of_schemes,
    make_action_with_db,
)

NEW_DATABASE = "auto"


@pytest.fixture(scope="class", autouse=False)
def setup():
    check_if_schema_exists("auto")
    print("Checking the initial list of databases:")
    get_list_of_schemes(print_result=1)
    try:
        print("adding the new database: {}".format(NEW_DATABASE))
        make_action_with_db(NEW_DATABASE, hostname="localhost")
    except Exception as general_exception:
        print(general_exception)
        print("The tested Database exists already")
    print("The updated list of databases")
    updated_schema_list = get_list_of_schemes(print_result=1)
    assert "auto" in updated_schema_list


@pytest.fixture()
def introduction():
    print("Start pytest")
    yield
    print("restoring the initial list of databases")
    make_action_with_db("auto", action_with_db="drop", hostname="localhost")
    restored_list_of_schemas = get_list_of_schemes()
    assert "auto" not in restored_list_of_schemas
    print(restored_list_of_schemas)
    print("Test is finished")
