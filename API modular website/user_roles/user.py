from request.user_req import ReqClass
from util.json_functions import JsonClass
from util.clear_screen import ClearScreenClass
from display_menu.all_menu import show_user_menu
from util.helper import Helper
from configuration import label

user_data_file = "database/userdata.json"
config_data = JsonClass.read_json("configuration/config.json")


class UserClass(ReqClass):
    def __init__(self, username):
        self.username = username
        print(f"Welcome {self.username}")

    def browse_website(self):
        ClearScreenClass.clear_screen()
        website = input(label.common_labels.get("ask_website"))
        if Helper.is_website_blocked(website, self.username):
            print(label.common_labels.get("blocked_website_message"))
        else:
            print(f"welcome to {website}")

    def show_blocked(self):
        # clear screen
        ClearScreenClass.clear_screen()
        blocked_website_list = Helper.get_blocked_websites(self.username)
        return blocked_website_list

    def add_web(self,new_web):
            data = JsonClass.read_json(user_data_file)
            user_list = data["user_details"]
            for item in user_list:
                if item.get("username") == self.username:
                    item["blocked"].append(new_web)

            # writing data
            JsonClass.write_data(user_data_file, data)
            return True

    def show_menu(self, role="user"):
        while True:
            show_user_menu()
            try:
                userinput = int(input())
                if userinput not in config_data.get("USER_MENU_LIST"):
                    print(label.common_labels.get("valid_number"))
                    continue
            except ValueError:
                print(label.common_labels.get("value_error_message"))
                continue
            except Exception as occurred_exception:
                print(occurred_exception)
                print(label.common_labels.get("valid_number"))
                continue
            
            match userinput:
                case 5:
                    break
                case 4:
                    user_input = input(label.user_labels.get("user_request_options"))
                    if user_input == '1':
                        ReqClass.req_func(self.username)
                    else:
                        print(label.common_labels.get("invalid_choice_error"))
                case 3:
                    self.add_web()
                case 2:
                    self.show_blocked()
                case 1:
                    self.browse_website()
