# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:QQ19981212@127.0.0.1/python'
#
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password= db.Column(db.String(80), unique=False, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=True)
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
# class Role(db.Model):
#     __tablename__ = 'roles'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User', backref='role')
#
#     def __repr__(self):
#         return "<Role %r>"%self.name