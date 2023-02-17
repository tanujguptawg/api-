from flask_smorest import Blueprint
from flask import request
from user_roles.admin import AdminClass
from auth.signup import SignupClass
from auth.login import LoginClass
from schema import SignupSchema,LoginSchema
from flask.views import MethodView
from models import UserDetails
from db import db
from sqlalchemy.exc import SQLAlchemyError
from flask_smorest import abort
blp = Blueprint("auth",__name__,description = "auth operations")

@blp.delete("/admin/remove_user")
def remove_user_api():
    data = request.get_json()
    username = data["username"]
    remove_user_id = data["remove_user_id"]
    obj = AdminClass(username)
    if obj.remove_user(remove_user_id):
        return {"message":"user removed successfully"},200

    return {"message":"this username does not exists "},500

@blp.route("/auth/signup")
class Auth(MethodView):
    @blp.arguments(SignupSchema)
    def post(self,data):

        username = data["name"]
        password = data["password"]
        conf_password=data["conf_password"]
        
        error_code = SignupClass.user_signup(username,password,conf_password)
        print(error_code)
        match error_code:
            case 1:
                return {"message":"user ID already Present "},200
            case 2:
                return {"message":"password length too short "},200
            case 3:
                return {"message":"passwords do not match "},200
        


@blp.route('/detail/<string:id>')
class Gagan(MethodView):
    @blp.response(200,SignupSchema)
    def get(self,id):
        # obj = UserDetails.query.filter_by(id=id).first()
        obj=UserDetails.query.get_or_404(id)
        if obj:
            return obj,200
        else:
            return {"message":"user not found"},404

@blp.post("/auth/login")
@blp.arguments( LoginSchema)
def login_func(data):
    username = data["username"]
    password = data["password"]
    if LoginClass.login_func(username,password):
        return {"message":"user found"},200
    
    return {"message":"user not found"},404
