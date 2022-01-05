from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# https://www.youtube.com/watch?v=1oOefRD8jek

# https://pythonhosted.org/Flask-Mail/

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "hello042hello@gmail.com"
app.config['MAIL_PASSWORD'] = "my_password"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/send_message', methods=["GET", "POST"])
def send_message():
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']

        message = Message(
            subject, sender="hello042hello@gmail.com", recipients=[email])
        message.body = msg
        mail.send(message)
        success = "Message Sent"
        return render_template('result.html', success=success)


if __name__ == "__main__":
    app.run(debug=True)


#  If you got an SMTP Authentication Error but
#  your user name / pass was correct. Here is what fixed it. Read this:

# https://support.google.com/accounts/answer/6010255

# In a nutshell, google is not allowing you to log in via smtplib because it has flagged this sort of login as "less secure",
#  so what you have to do is go to this link while you're logged in to your google account, and allow the access:

# https://www.google.com/settings/security/lesssecureapps     , turn it on from this link

# Once that is set , it should work.
