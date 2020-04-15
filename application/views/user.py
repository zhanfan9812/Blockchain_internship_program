from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from application.models import User

user_page = Blueprint('user_page', __name__)

@user_page.route("/<page>.html")
def to_login(page):
    return render_template(page+'.html')

@user_page.route('/users')
def users():
    if session.get('user_id'):
        return render_template('/index.html',role=session.get('user_role') ,username=session.get('user_name'))
    else:
        return redirect('/')

@user_page.route('/')
@user_page.route('/login', methods=['GET', 'PoSt'])
def login():
    if request.method == 'GET':
        print('get_arrive')
        return render_template('/login.html')
    else:
        print('post_arrive')
        name = request.form.get('username')
        pwd = request.form.get('password')

        user = User.query.filter(User.username == name).first()
        print('name:',name,'pwd:',pwd)
        print(user)
        # print('user.password:', user.password)
        if user and user.password == pwd:
            session['user_id'] = user.id
            session['user_role'] = user.role
            session['user_name'] = user.username
            # print('登录成功')
            # return redirect(url_for('user_page.users'))
            return '1'
        else:
            return '0'
            # print('登录失败')
            # return render_template('user/login.html')
