from ..resource_dir import resourse_data
from ..resource_dir.requests import adding_user, get_page_data
from ..resource_dir.users_data import NEW_USER


class TestClassAddingUsersPage:

    TESTED_PAGE = "/api/users"
    ENV_URL = resourse_data.BASE_URL
    ENDPOINT = ENV_URL + TESTED_PAGE

    def test_adding_user_code_is_201(self, request):
        """Test checks the response code of adding new user"""
        response_code, _ = adding_user(
            endpoint=request.cls.ENDPOINT,
            user_city=NEW_USER["city"],
            user_email="test_201_" + NEW_USER["email"],
            first_name=NEW_USER["name"],
            last_name="test_201_" + NEW_USER["last_name"],
        )
        checked_value = response_code == 201
        print("The response code = 201 is: {}".format(checked_value))
        assert checked_value

    def test_adding_user_enlarge_list_of_users(self, request):
        """Test checks the number of users after adding new user"""
        _, initial_list = get_page_data(request.cls.ENDPOINT)
        initial_list_length = len(initial_list)
        _, adding_response = adding_user(
            endpoint=request.cls.ENDPOINT,
            user_city=NEW_USER["city"],
            user_email="test_users_list_" + NEW_USER["email"],
            first_name=NEW_USER["name"],
            last_name="test_users_list_" + NEW_USER["last_name"],
        )
        _, modified_list = get_page_data(request.cls.ENDPOINT)
        modified_list_length = len(modified_list)
        assert initial_list_length + 1 == modified_list_length
