from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

all_posts = [
    {"title": "post 1",
     "content": "This is post 1"},
    {"title": "post 2",
     "content": "This is post 2"}]


@app.route('/')
def index():
    return render_template('post.html', posts=all_posts)
    # we can access this data(all_posts) in post.html using posts 

# custom filter take date and show in ( 03 Apr 2021 ) format
@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")  # 03 Apr 2021

@app.route("/jinja")
def jinja():

    # Strings
    my_name = "Nouman"

    # Integers
    my_age = 30

    # html string
    my_html = "<h1>This is some HTML</h1>"

    # Lists
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C", "Rust"]

    # Dictionaries
    friends = {
        "Ali": 43,
        "Humza": 28,
        "Syed": 26,
        "Farhan": 23,
        "Fatima": 39
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    bool_var = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description
            self.domain = domain

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/Julian-Nash/learning-flask.git"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    date = datetime.utcnow()

    suspicious = "<script>alert('NEVER TRUST USER INPUT!')</script>"

    return render_template( "jinja.html", var1=my_name, my_age=my_age, langs=langs,
        friends=friends, colors=colors, bool_var=bool_var, GitRemote=GitRemote,
        my_remote=my_remote, repeat=repeat, date=date , my_html=my_html , suspicious = suspicious
        )


if __name__ == "__main__":
    app.run(debug=True)
