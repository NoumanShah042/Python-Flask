from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world!"


# app.run()


@app.route("/nouman")
def intro():
    return "hello Nouman!"


app.run(debug=True)
