from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from application.extension import db
from flask import jsonify
from application.models import User

admin_page = Blueprint('admin_page', __name__)

@admin_page.route('/select_username',methods=["POST"])
def select_username():
    username = request.form.get('username')
    role = request.form.get('role')
    user = User.query.filter(User.username == username,User.role == role).first()
    if (user is None):
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
    if (username == "")| (password == "") | (email == ""):
        return '0_1'
    if User.query.filter(User.username == username).first():
        return '0_2'
    if User.query.filter(User.email == email).first():
        return '0_3'
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

    if (username == "")| (password == "") | (email == ""):
        return '0_1'
    if User.query.filter(User.username == username,User.id != id).first():
        return '0_2'
    if User.query.filter(User.email == email,User.id != id).first():
        return '0_3'
    user = User.query.get(id)
    user.username = username
    user.password = password
    user.email = email
    user.gender = gender
    user.role = role

    db.session.commit()
    return '1'

@admin_page.route('/update_personal',methods=["POST"])
def update_personal():
    password = request.form.get('password')
    email = request.form.get('email')
    gender = request.form.get('gender')
    id = request.form.get('id')
    if  (password == "") | (email == ""):
        return '0_1'
    if User.query.filter(User.email == email,User.id != id).first():
        return '0_3'
    user = User.query.get(id)
    user.password = password
    user.email = email
    user.gender = gender
    db.session.commit()
    return '1'

@admin_page.route('/getinfo',methods=["POST"])
def getinfo():
    id = request.form.get('id')
    user = User.query.filter(User.id == id).first()
    data = {
        'username': user.username,
        'role': user.role,
        'email': user.email,
        'password': user.password,
        'gender': user.gender
    }
    return jsonify(data)

@admin_page.route("/role/getCountByRole/<role>")
def getCountByRole(role):
    role = int(role)
    count = User.query.filter(User.role==role).count()
    return str(count)

@admin_page.route("/role/getRoleByRolePage/<role>/<curr>/<limit>")
def getRoleByRolePage(role,curr,limit):
    role = int(role)
    curr = int(curr)
    limit = int(limit)
    users = User.query.filter(User.role==role).offset((curr-1)*limit).limit(limit)
    data = []
    for user in users:
        user_dict = {
            'username': user.username,
            'id': user.id,
            'email': user.email,
            'gender': user.gender
        }
        data.append(user_dict)
    return jsonify({"data": data})