from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from flask import jsonify
from application.models import User
import  json

admin_page = Blueprint('admin_page', __name__)

@admin_page.route('/select_username',methods=["POST"])
def select_username():
    name = request.form.get('username')
    print(name)
    user = User.query.filter(User.username == name).first()
    print(user)
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
