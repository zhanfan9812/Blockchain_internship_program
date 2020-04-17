from flask import Flask
from application.extension import db
from application.views.user import user_page
from application.views.logistician import logistician_page
import os

app = Flask('Blockchain_internship_program')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:QQ19981212@127.0.0.1/python'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

app.secret_key = "lalskskskskksksjsj"

db.init_app(app)

app.register_blueprint(user_page)
app.register_blueprint(logistician_page)
#set FLASK_APP=application.__init__.py
#set FLASK_ENV=development