from util.json_functions import JsonClass
from util.clear_screen import ClearScreenClass
from configuration.label import user_labels
from util.helper import Helper
from configuration.label import common_labels
request_data_file = "database/requests.json"
user_data_file = "database/userdata.json"


class ReqClass:

    @staticmethod
    def req_func(username):
        ClearScreenClass.clear_screen()
        req_web = input(user_labels.get("unblock_web_request"))
        blocked_website_list = Helper.get_blocked_websites(username)
        if req_web not in blocked_website_list[0]:
            print(common_labels.get("website_already_blocked"))
        else:
            try:
                # reading data
                data = JsonClass.read_json(request_data_file)
                data[username].append(req_web)
                # writing data
                JsonClass.write_data(request_data_file, data)

            except Exception as new_exception:
                print(new_exception)
                try:
                    # reading data
                    data = JsonClass.read_json(request_data_file)
                    data[username] = [req_web]
                    # writing data
                    JsonClass.write_data(request_data_file, data)
                except ValueError as inner_exception:
                    print(inner_exception)
                
