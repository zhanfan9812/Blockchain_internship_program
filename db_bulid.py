from __init__ import db
from models import User

if __name__=='__main__':
    db.create_all()  # 此语句只需在建表时执行
    print('表已创建')
    #初始化User表
    admin = User(username='admin', password='123456', role=0)
    db.session.add(admin)
    db.session.commit()

#增
# admin = User(username='admin1',password='123456')
# guest = User(username='fff', email='fff@example.com')
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()
#查
# users=User.query.all()
# for x in users:
#     print(x.username,x.password,x.email)
# print(User.query.filter_by(username='zzz').first())
# print(User.query.count())
# print(User.query.filter_by(username='a%'))
# print(User.query.filter(User.username=='a%').all())
#改
# user=User.query.get(15)
# user.email='ffff@example.com'
# #删
# db.session.delete(user)