# from flask import Flask,escape,request,url_for
#
# app = Flask(__name__)
#
# @app.route('/')
# @app.route('/hello/',endpoint='hello')
# def hello_world():
#     return url_for('hello')
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % escape(subpath)
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         print('do_the_login()')
#         return 'Hello, World! POST'
#     else:
#         print('show_the_login_form()')
#         return 'Hello, World!'
#
# if __name__=='__main__':
#     app.debug=True
#     app.run()
#     print(url_for('hello_world'))