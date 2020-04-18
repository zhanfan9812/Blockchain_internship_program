from flask import Flask
from application.extension import db
from application.views.user import user_page
from application.views.admin import admin_page
from application.views.item import producer_page
from application.views.warehouse import warehouse_page
from application.views.logistician import logistician_page
from application.models import User,Product
import os
import click

app = Flask('Blockchain_internship_program')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

app.secret_key = "lalskskskskksksjsj"

db.init_app(app)

app.register_blueprint(user_page)
app.register_blueprint(admin_page)
app.register_blueprint(logistician_page)
app.register_blueprint(warehouse_page)
app.register_blueprint(producer_page)

@app.cli.command()
def dbbuild():
    db.drop_all()
    db.create_all()
    admin1 = User(username='admin1', password='123456', role=1)
    admin2 = User(username='admin2', password='123456', role=2)
    admin3 = User(username='admin3', password='123456', role=3)
    admin4 = User(username='admin4', password='123456', role=4)
    product1 = Product(id=1,product_name='生产中的商品', status='1', number='1',date="20200202",description="00")
    product2 = Product(id=2,product_name='待运输的商品', status='2', number='2',date="20200202",description="00")
    product3 = Product(id=3,product_name='运输中的商品', status='3', number='3',date="20200202",description="00")
    product4 = Product(id=4,product_name='已到达的商品', status='4', number='4',date="20200202",description="00")
    product5 = Product(id=5,product_name='已入库的商品', status='5', number='5',date="20200202",description="00")
    db.session.add(admin1)
    db.session.add(admin2)
    db.session.add(admin3)
    db.session.add(admin4)
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    db.session.commit()
    click.echo('表已初始化.')