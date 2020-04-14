from .__init__ import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.Integer, nullable=False)    #0:管理员 1:生产商 2:物流人员 3:仓库人员


    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.username
