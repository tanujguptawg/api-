from db import db

class UserDetails(db.Model):
    __tablename__ = 'user_details'

    id = db.Column(db.Integer, primary_key=True)
    role_type=db.Column(db.Integer,db.ForeignKey("roles.id"))
    name=db.Column(db.String(80),nullable=False,unique=True)
    password=db.Column(db.String(256),nullable=False)

    role_conn_var = db.relationship("Role",back_populates="user_details_conn_var")
    block_conn_var = db.relationship("BlockWeb",back_populates="user_conn_var")
    
