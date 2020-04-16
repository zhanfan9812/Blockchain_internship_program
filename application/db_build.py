from application.__init__ import app
from application.extension import db
from application.models import User
from application.models import Product

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        admin1 = User(username='admin1', password='123456', role=1)
        admin2 = User(username='admin2', password='123456', role=2)
        admin3 = User(username='admin3', password='123456', role=3)
        admin4 = User(username='admin4', password='123456', role=4)
        product1 = Product(product_name='生产中的商品', status='1', number='1')
        product2 = Product(product_name='待运输的商品', status='2', number='2')
        product3 = Product(product_name='运输中的商品', status='3', number='3')
        product4 = Product(product_name='已到达的商品', status='4', number='4')
        product5 = Product(product_name='已入库的商品', status='5', number='5')
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
    print('表已初始化')
#初始化User表