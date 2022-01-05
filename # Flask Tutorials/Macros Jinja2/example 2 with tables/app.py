from flask import Flask, render_template, request, make_response

app = Flask(__name__)

headings = ("Name", "Role", "Salary", "Department")

data = (

    ("Rolf", "Software Engineer", "E42, 000.00", "Engineering"),
    ("Amy", "Product Owner", "€55, 000.00", "Engineering"),
    ("Adam", "Software Engineer", "E49, 000.00", "Engineering"),
    ("Helen", "Product Owner", "€49, 000.00", "Engineering"),
    ("Humza", "Security Engineer", "€45, 000.00", "Engineering")
)


@app.route("/")
def component():
    return render_template("index.html", headings=headings, data=data)


if __name__ == '__main__':
    app.run(debug=True)
