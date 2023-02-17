import hashlib
from util.json_functions import JsonClass


class HashClass:

    @staticmethod
    def hash_func(password):

        # reading config data
        config_data = JsonClass.read_json("configuration/config.json")

        # take salt value from config
        salt = config_data["SALT"]
    
        # Adding salt at the last of the password
        salted_password = password + salt

        # Encoding the password
        hashed = hashlib.sha512(salted_password.encode())
        hashed_pass = hashed.hexdigest()

        return hashed_pass
