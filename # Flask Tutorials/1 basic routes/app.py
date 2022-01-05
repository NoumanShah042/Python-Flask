from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'hello world'


# ****************************

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


# ****************************

@app.route('/blog/<int:postid>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<float:revno>')
def revision(revNo):
    return 'Revision Number %f' % revNo


# http://127.0.0.1:5000/blog/11
# http://localhost:5000/rev/1.1

# ****************************
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


# http://127.0.0.1:5000/admin
# http://127.0.0.1:5000/guest/ednalan
# http://127.0.0.1:5000/guest/ednalan
# ****************************
if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/hello
