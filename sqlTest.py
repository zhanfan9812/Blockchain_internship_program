from test import db
from test import User
db.create_all()
admin = User(username='t', email='t@example.com')
guest = User(username='bttbb', email='bttbb@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
print(User.query.all())