from application.extension import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.Integer, nullable=False)    #1:生产商 2:物流人员 3:仓库人员 4:管理员
    email = db.Column(db.String(120), unique=True)
    gender = db.Column(db.String(120))

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


    def __repr__(self):
        return '<User username:%r>' % self.username

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False) #1:生产中 2:待运输 3：运输中 4：已到达 5：已入库
    number = db.Column(db.Integer, nullable=False)
    date_of_pro = db.Column(db.DateTime, nullable=False, default=datetime.now)
    description = db.Column(db.Text)
    block_info = db.Column(db.Text)

    def __init__(self, product_name, status, number, description):
        self.product_name = product_name
        self.status = status
        self.number = number
        self.description = description

    def __repr__(self):
        return '<Product product_name:%r>' % self.product_name


class Logistic(db.Model):
    __tablename__ = 'logistics'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False)  #1:生产中 2:待运输 3：运输中 4：已到达 5：已入库
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    operator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    random_num = db.Column(db.Integer)
    current_hash = db.Column(db.String(200))
    pre_hash = db.Column(db.String(200))
    chain_index = db.Column(db.Integer)
    description = db.Column(db.Text)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, product_id, status):
        self.product_id = product_id
        self.status = status

    def __repr__(self):
        return '<Logistic id:%r status:%s product_id:%s>' % (self.id, self.status, self.product_id)