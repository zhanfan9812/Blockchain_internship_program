from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from application.models import User

user_page = Blueprint('user_page', __name__)


@user_page.route('/users')
def users():
    if session.get('user_id'):
        users = User.query.all()
        return render_template('user/index.html', users=users)
    else:
        return redirect('/')


@user_page.route('/')
@user_page.route('/login', methods=['GET', 'PoSt'])
def login():
    if request.method == 'GET':
        print('get_arrive')
        return render_template('user/login.html')
    else:
        print('post_arrive')
        name = request.form.get('name')
        pwd = request.form.get('password')

        user = User.query.filter(User.username == name).first()
        print('pwd:',pwd)
        # print('user.password:', user.password)
        if user and user.password == pwd:
            session['user_id'] = user.id
            # return redirect(url_for('user_page.users'))
            return '1'
        else:
            # flash('登陆失败')
            return '0'
            # return render_template('user/login.html')
