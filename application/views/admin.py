from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from application.extension import db
from flask import jsonify
from application.models import User
import  json

admin_page = Blueprint('admin_page', __name__)

@admin_page.route('/select_username',methods=["POST"])
def select_username():
    username = request.form.get('username')
    role = request.form.get('role')
    user = User.query.filter(User.username == username,User.role == role).first()
    if (user == None):
        return '0'
    data = {
        'username' : user.username,
        'id' : user.id,
        'email': user.email,
        'gender': user.gender
    }
    return jsonify(data)
    # return '{username:lilin}'

@admin_page.route('/select_role',methods=["POST"])
def select_role():
    role = request.form.get('role')
    users = User.query.filter(User.role==role).all()
    data = []
    for user in users:
        user_dict = {
            'username' : user.username,
            'id' : user.id,
            'email': user.email,
            'gender': user.gender
        }
        data.append(user_dict)
    return jsonify({"data": data})

@admin_page.route('/delete_id',methods=["POST"])
def delete_id():
    id = request.form.get('id')
    user = User.query.get(id)
    if (user is None):
        return '0'
    else:
        db.session.delete(user)
        db.session.commit()
        return '1'

@admin_page.route('/add',methods=["POST"])
def add():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    gender = request.form.get('gender')
    role = request.form.get('role')
    if (username == "")| (password == "") | (role == ""):
        return '0'
    if User.query.filter(User.username == username).first():
        return '0'
    user = User(username=username, password=password, email=email, gender=gender, role=role)
    db.session.add(user)
    db.session.commit()
    return '1'

@admin_page.route('/update_id',methods=["POST"])
def update_id():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    gender = request.form.get('gender')
    role = request.form.get('role')
    id = request.form.get('id')

    if (username == "")| (password == "") | (role == ""):
        return '0'
    if User.query.filter(User.username == username).first():
        return '0'
    user = User.query.get(id)
    user.username = username
    user.password = password
    user.email = email
    user.gender = gender
    user.role = role

    db.session.commit()
    return '1'