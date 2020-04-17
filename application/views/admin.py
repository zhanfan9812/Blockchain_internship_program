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
    data1 = {
        'username':user.username,
        'age':'18'
    }
    data2 = {
        'username': 'lili',
        'age': '18'
    }
    data = [data1,data2]
    return jsonify({"data":data})
    # return '{username:lilin}'