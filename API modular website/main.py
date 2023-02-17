from auth.login import LoginClass
from auth.signup import SignupClass
from util import clear_screen
from display_menu.all_menu import show_home_menu
from util.json_functions import JsonClass
from configuration.label import common_labels


config_file_name = "configuration/config.json"
config_data = JsonClass.read_json(config_file_name)

while True:
    clear_screen.ClearScreenClass()
    show_home_menu()
    try:
        user_input = int(input())
        if user_input not in config_data.get("HOME_MENU_LIST"):
            print(common_labels.get("valid_number"))
            continue
    except ValueError:
        print(common_labels.get("value_error_message"))
        continue
    except Exception as new_exception:
        print(f"please enter valid number error occurred {new_exception}")
        continue
    
    match user_input:
        case 1:
            LoginClass.login_func()
        case 2:
            SignupClass.user_signup()
        case 3:
            break
