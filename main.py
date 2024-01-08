from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask("__name__")
app.secret_key = "you_can_provide_your_own_secret_key_string"


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="log IN")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    my_form = LoginForm()
    my_form.validate_on_submit()
    return render_template("login.html", form=my_form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
