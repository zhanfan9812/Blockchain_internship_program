from test import db
from test import User,Role
db.drop_all()
db.create_all()
# 增
admin = User(username='admin1',password='123456')
guest = User(username='fff', email='fff@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
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

# db.session.commit()
# admin_role = Role(name='Admin')
# mod_role = Role(name='Moderator')
# user_role = Role(name='User')
# user_john = User(username='john', password='john',role=admin_role)
# user_susan = User(username='susan', password='susan',role=user_role)
# user_david = User(username='david',password='david', role=user_role)
#
# db.session.add(admin_role)
# db.session.add(mod_role)
# db.session.add(user_role)
# db.session.add(user_john)
# db.session.add(user_susan)
# db.session.add(user_david)
admin_role = Role.query.get(3)
print(admin_role.users)

db.session.commit()