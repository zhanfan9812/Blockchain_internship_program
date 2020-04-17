from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from application.extension import db
from flask import jsonify
from application.models import User
import  json

admin_page = Blueprint('admin_page', __name__)

@admin_page.route('/select_username',methods=["POST"])
def select_username():
    name = request.form.get('username')
    role = request.form.get('role')
    user = User.query.filter(User.username == name,User.role == role).first()
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
    user = User.query.filter(User.id == id).first()
    if (user == None):
        return '1'
    else:
        db.session.delete(user)
        db.session.commit()
        return '0'