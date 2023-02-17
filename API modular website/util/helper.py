from util.json_functions import JsonClass
import os

config_data = JsonClass.read_json("configuration/config.json")
user_data_file = os.getcwd() + "\\database\\" + config_data["USER_DATA_FILE"]


class Helper:
    @staticmethod
    def is_user_present(name):
        existing_user_list = []
        data = JsonClass.read_json(user_data_file)
        user_list = data["user_details"]
        for item in user_list:
            existing_user_list.append(item["username"])

        if name in existing_user_list:
            return True
        else:
            return False

    @staticmethod
    def is_correct_password(password, confirmed_password):
        if password == confirmed_password:
            return True
        return False

    @staticmethod
    def check_password_length(password):
        if len(password) >= config_data["PASSWORD_LENGTH"]:
            return True
        return False

    @staticmethod
    def is_admin(role):
        if role == "admin":
            return True
        else:
            return False

    @staticmethod
    def is_website_blocked(website, username):
        loaded_data = JsonClass.read_json(user_data_file)
        user_list = loaded_data["user_details"]
        blocked_website_list = []

        for item in user_list:
            if item["username"] == username:
                blocked_website_list = (item["blocked"])
        
        if website in blocked_website_list:
            return True
        else:
            return False

    @staticmethod
    def get_blocked_websites(username):
        loaded_data = JsonClass.read_json(user_data_file)
        user_list = loaded_data["user_details"]
        blocked_website_list = []

        for item in user_list:
            if item["username"] == username:
                blocked_website_list.append(item["blocked"])
        return blocked_website_list

    @staticmethod
    def get_user_role(username):
        data = JsonClass.read_json(user_data_file)
        for item in data["user_details"]:
            if item["username"] == username:
                return item["role"]
