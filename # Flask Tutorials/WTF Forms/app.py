from flask import Flask, render_template, flash,   redirect,url_for
from forms import ContactForm

app = Flask(__name__)

app.secret_key = 'cairocoders-ednalan-456895'


# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     form = ContactForm()
#     if form.validate() == False:
#         flash('All fields are required.')
#     return render_template('contact.html', form=form)

@app.route("/contact", methods=['GET', 'POST'])
def register():
    form = ContactForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.email.data)
        print(form.gender.data)
        print(form.language.data)
        print(form.password.data)
        print(form.confirm_password.data)

        return redirect(url_for('success'))   # we have passed function name , not route
    return render_template('contact.html',  form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True)
