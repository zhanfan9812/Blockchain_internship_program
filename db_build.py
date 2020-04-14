from extension import db
from models import User
from __init__ import app

with app.app_context():
    db.create_all()
    admin = User(username='admin', password='123456', role=0)
    db.session.add(admin)
    db.session.commit()
print('表已创建')
#初始化User表