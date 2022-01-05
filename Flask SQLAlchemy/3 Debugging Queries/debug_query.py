from flask import Flask, render_template, url_for, request

from model import User

from flask.ext.sqlalchemy import get_debug_queries

app = Flask(__name__)


@app.route('/')
def index():
    a = User.query.filter_by(name='nouman').first()


def sql_debug(response):
    queries = list(get_debug_queries())
    query_str = ''
    total_duration = 0.0
    for q in queries:
        total_duration += q.duration
        stmt = str(q.statement % q.parameters).replace('\n', '\n       ')
        query_str += 'Query: {0}\nDuration: {1}ms\n\n'.format(
            stmt, round(q.duration * 1000, 2))

    print('=') * 80
    print(' SQL Queries - {0} Queries Executed in {1}ms').format(
        len(queries), round(total_duration * 1000, 2))
    print('=') * 80
    print(query_str.rstrip('\n'))
    print('=') * 80 + '\n'

    return response


app.after_request(sql_debug)

if __name__ == '__main__':
    app.run(debug=True)
