from flask import Flask
from application.extension import db
from application.views.user import user_page
from application.views.admin import admin_page
from application.views.item import producer_page
from application.views.warehouse import warehouse_page
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
app.register_blueprint(warehouse_page)
app.register_blueprint(producer_page)

@app.cli.command()
def dbbuild():
    db.drop_all()
    db.create_all()
    admin1 = User(username='admin1', password='pbkdf2:sha1:1000$X97hPa3g$252c0cca000c3674b8ef7a2b8ecd409695aac370', role=1, email='admin1@163.com', gender='1')
    admin2 = User(username='admin2', password='pbkdf2:sha1:1000$X97hPa3g$252c0cca000c3674b8ef7a2b8ecd409695aac370', role=2, email='admin2@163.com', gender='0')
    admin3 = User(username='admin3', password='pbkdf2:sha1:1000$X97hPa3g$252c0cca000c3674b8ef7a2b8ecd409695aac370', role=3, email='admin3@163.com', gender='1')
    admin4 = User(username='admin4', password='pbkdf2:sha1:1000$X97hPa3g$252c0cca000c3674b8ef7a2b8ecd409695aac370', role=4, email='admin4@163.com', gender='0')
    product1 = Product(product_name='生产中的商品', status='1', number='1', description='description1')

    product2 = Product(product_name='待运输的商品', status='2', number='2', description='description2')

    product3 = Product(product_name='运输中的商品', status='3', number='3', description='description3')

    product4 = Product(product_name='已到达的商品', status='4', number='4', description='description4')

    product5 = Product(product_name='已入库的商品', status='5', number='5', description='description5')
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