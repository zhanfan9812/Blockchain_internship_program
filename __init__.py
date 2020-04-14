from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views.user import user_page


app = Flask('Blockchain_internship_program')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:QQ19981212@127.0.0.1/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "lalskskskskksksjsj"

db = SQLAlchemy(app)
app.register_blueprint(user_page)


