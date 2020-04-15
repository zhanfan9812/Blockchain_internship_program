from application.__init__ import app
from application.extension import db
from application.models import User

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        admin = User(username='admin', password='123456', role=4)
        db.session.add(admin)
        db.session.commit()
    print('表已创建')
#初始化User表