from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/', defaults={"name": 'world'})
@app.route('/hello/<name>', endpoint='hello')
def index(name):
    return render_template('index.html', name=name)


@app.route('/login', methods=['GET', 'PoSt'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form.get('name')
        pwd = request.form.get('password')
        if name == 'admin' and pwd == '123456':
            return 'login successed!'
        else:
            return 'login failed!!!'
