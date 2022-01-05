from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# youtube.com/watch?v=hkL9pgCJPNk

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pages.db'

db = SQLAlchemy(app)


class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))


@app.route('/')
def main_():
    return "/thread/1"


@app.route('/thread/<int:page_num>')
def thread(page_num):
    # pagination notes ->  D:\Python_ Flask programming\Corey Schafer\09_pagination

    threads = Thread.query.paginate(per_page=5, page=page_num, error_out=False)

    return render_template('index.html', threads=threads)

# ************

# error_out  by default is True , show error in case of page error

# if error_out  is False , web page show only links to other pages in case of errors
# http: // 127.0.0.1: 5000/thread/43

# ************


if __name__ == '__main__':
    app.run(debug=True)
