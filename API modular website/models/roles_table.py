from db import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role_types = db.Column(db.String(64), unique=True,nullable=False)

    user_details_conn_var = db.relationship("UserDetails",back_populates="role_conn_var")
    