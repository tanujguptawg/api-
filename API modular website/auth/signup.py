"""to hide passwords"""
import getpass
from util.json_functions import JsonClass
from util.hash_code import HashClass
from util.helper import Helper
from configuration.label import common_labels
config_data = JsonClass.read_json("configuration/config.json")
from db import db
from models import UserDetails
from sqlalchemy.exc import SQLAlchemyError
from flask_smorest import abort

class SignupClass:

    @staticmethod
    def add_new_user(new_user_name, hashed_password):
        data = {"name": new_user_name, "password": hashed_password, "role_type": 2}
        user=UserDetails(**data)
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            abort(500,message="Error wjkfhwsiofhvwe")
        return {"messgae": "gfffgfj"}

    @staticmethod
    def user_signup(user_id,password,conf_password):

        if not Helper.check_password_length(password):
            return 2

        if not Helper.is_correct_password(password, conf_password):
            return 3
        hashed_password = HashClass.hash_func(password)
        SignupClass.add_new_user(user_id,hashed_password)
        return 0
