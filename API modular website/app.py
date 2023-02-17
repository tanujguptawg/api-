from flask import Flask,request
# from auth.login import LoginClass
# from auth.signup import SignupClass
# from user_roles.admin import AdminClass
from flask_smorest import Api
from auth.routes import blp as authblueprint
import os 
from db import db 
import models 
    
def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(authblueprint)
    return app
    
    # @app.get("/")
# def root():
#     return("hello")
    

# @app.delete("/admin/remove_user")
# def remove_user_api():
#     data = request.get_json()
#     username = data["username"]
#     remove_user_id = data["remove_user_id"]
#     obj = AdminClass(username)
#     if obj.remove_user(remove_user_id):
#         return {"message":"user removed successfully"},200

#     return {"message":"this username does not exists "},500

# @app.get("/admin/show_blocked/<string:name>")
# def show_blocked(name):
#     obj = AdminClass(name)
#     return obj.show_blocked()

# @app.post("/user/add_web")
# def add_web():
#     data = request.get_json()
#     username = data["username"]
#     new_web = data["new_web"]

#     obj =  AdminClass(username)
#     if obj.add_web(new_web):
#         return {"message":"website added succesfully"},200
    
#     return {"message":"error"},500


    
    

