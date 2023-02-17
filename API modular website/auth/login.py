import getpass
from user_roles.user import UserClass
from user_roles.admin import AdminClass
from util.clear_screen import ClearScreenClass
from util.json_functions import JsonClass
from util.hash_code import HashClass
from configuration.label import common_labels
user_data_file = "database/userdata.json"
config_data = JsonClass.read_json("configuration/config.json")


class LoginClass:

    def __init__(self):
        ClearScreenClass.clear_screen()

    @staticmethod
    def login_func(username,password):
        login_id = username
        password = password
        hashed_pass = HashClass.hash_func(password=password)
        filename="database/userdata.json"
        data = JsonClass.read_json(filepath=filename)
        for user in data["user_details"]:
            if user["username"] == login_id and user["password"] == hashed_pass:
                return True

        return False