from db import db

class BlockWeb(db.Model):
    __tablename__ = 'block_web'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user_details.id'))
    blocked=db.Column(db.String(80),nullable=False)
    request=db.Column(db.Boolean,nullable=False)

    user_conn_var = db.relationship("UserDetails",back_populates="block_conn_var")

