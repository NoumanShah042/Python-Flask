from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['DEBUG'] = True

db = SQLAlchemy(app)


class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


@app.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    try:
        post = Blogpost.query.filter_by(id=post_id).one()
        print("hello")
        if post:
            print("posted")
            return render_template('post.html', post=post)
        else:
            return redirect(url_for('index'))
    except:
        return redirect(url_for('index'))


@app.route('/delete_post/<int:post_id>')
def delete_post(post_id):
    try:
        delete_this = Blogpost.query.filter_by(id=post_id).one()
        if delete_this:
            db.session.delete(delete_this)
            db.session.commit()
        return redirect(url_for('index'))
    except:
        return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
