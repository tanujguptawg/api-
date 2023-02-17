from display_menu.all_menu import show_admin_menu
from user_roles.user import UserClass
from auth.signup import SignupClass
from util.json_functions import JsonClass
from util.clear_screen import ClearScreenClass
from util.helper import Helper
from configuration import label

user_data_file = "database/userdata.json"
request_data_file = "database/requests.json"
config_data = JsonClass.read_json("configuration/config.json")


class AdminClass(UserClass):
    def __init__(self, username):
        self.username = username
        print(f"welcome {self.username}")

    def remove_user(self,user_ID):
        
        if not Helper.is_user_present(user_ID):
            return False
      
        data = JsonClass.read_json(user_data_file)
        for item in data.get("user_details"):
            if item.get("username") == user_ID:
                data["user_details"].remove(item)
                break
        # writing data
        JsonClass.write_data(user_data_file, data)
        return True

    def check_details(self):
        ClearScreenClass.clear_screen()
        # reading data
        data = JsonClass.read_json(user_data_file)
        user_list = data["user_details"]
        for item in user_list:
            user = item["username"]
            role = item["role"]
            print(f"{user} - > {role}")

    def change_role(self):
        user = input(label.admin_labels.get("change_role_input"))
        if not Helper.is_user_present(user):
            print(label.common_labels.get("user_not_exists"))
            return
        
        print(f"are you sure you want to change role for {user} ")
        label.common_labels.get("confirm_message")
        conf = input(label.admin_labels.get("change_role_choices"))
        if conf != "y":
            return
            
        # reading data
        user_role = Helper.get_user_role(user)
        print(f"current role of {user} is {user_role}")
        label.admin_labels.get("change_role_choices")
        try:
            choice = int(input(label.common_labels.get("enter_choices")))
            match choice:
                case 1:
                    if Helper.is_admin(user_role):
                        label.admin_labels.get("already_admin")
                        return 
                    data = JsonClass.read_json(user_data_file)
                    for item in data["user_details"]:
                        if item.get("username") == user and item.get("role") == "user":
                            item["role"] = "admin"
                            print(f"{user} ROLE CHANGED SUCCESSFULLY")
                case 2:
                    if not Helper.is_admin(user_role):
                        label.user_labels.get("already_user")
                    data = JsonClass.read_json(user_data_file)
                    for item in data["user_details"]:
                        if item.get("username") == user and item.get("role") == "admin":
                            item["role"] = "user"
                            print(f"{user} ROLE CHANGED SUCCESSFULLY")
                    JsonClass.write_data(user_data_file, data)
                case _:
                    input(label.common_labels.get("invalid_choice_error"))
        except ValueError:
            print(label.common_labels.get("value_error_message"))
        except Exception as new_exception:
            print(new_exception)
            input(label.common_labels.get("invalid_choice_error"))
                
    def unblock(self):
        unblock_web = input(label.admin_labels.get("unblock_web_message"))
        if not Helper.is_website_blocked(unblock_web, self.username):
            print(label.admin_labels.get("web_already_blocked"))
        else:
            print("are you sure you want to unblock this website ")
            conf = input(label.common_labels.get("confirm_message"))
            if conf == "y":
                # reading data
                data = JsonClass.read_json(user_data_file)
                for item in data.get("user_details"):
                    if item.get("username") == self.username:
                        item["blocked"].remove(unblock_web)

                JsonClass.write_data(user_data_file, data)
                print(f"{unblock_web} UNBLOCKED SUCCESSFULLY")

    def show_req(self):
        # reading data
        data = JsonClass.read_json(request_data_file)
        print(data)
        print(label.admin_labels.get("admin_show_request"))
        
        admin_input = input(label.common_labels.get("enter_choices"))
        if admin_input == '1':
            user_name = input(label.admin_labels.get("ask_resolve_request"))
            # check user in data base
            data = JsonClass.read_json(request_data_file)
            try:
                # for checking if user made a request earlier
                data[user_name]
                unblock_web = input(label.common_labels.get("ask_unblock_web"))
                try:
                    data[user_name].remove(unblock_web)
                    # writing data
                    JsonClass.write_data(request_data_file, data)
                    print("website removed successfully")
                    # now also removing from userdata file
                    data = JsonClass.read_json(user_data_file)
                    for item in data["user_details"]:
                        if item["username"] == user_name:
                            item["blocked"].remove(unblock_web)

                    # writing data
                    JsonClass.write_data(user_data_file, data)
                    
                except Exception as exception_occurred:
                    print(exception_occurred)
                    print("no such website in requests")

            except Exception as exception_occurred:
                print(exception_occurred)
                print(f"{user_name} has no requests")

    def show_menu(self, role="user"):
        while True:
            show_admin_menu()
            try:
                userinput = int(input("enter you choice"))
                if userinput not in config_data["ADMIN_MENU_LIST"]:
                    print(label.common_labels.get("valid_number"))
                    continue
            except Exception as new_exception:
                print(new_exception)
                print(label.common_labels.get("invalid_choice_error"))
                continue
            
            match userinput:
                case 10:
                    break
                case 9:
                    self.show_req()
                case 8:
                    self.change_role()
                case 7:
                    self.check_details()
                case 6:
                    self.remove_user()
                case 5:
                    SignupClass.user_signup()
                case 4:
                    self.unblock()
                case 3:
                    self.add_web()
                case 2:
                    self.show_blocked()
                case 1:
                    self.browse_website()
                case _:
                    print(" invalid input ")
