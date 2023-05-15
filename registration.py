from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Process the form data, e.g., save the user to the database
        # Here, we'll just print the submitted data
        print(f"Username: {form.username.data}")
        print(f"Email: {form.email.data}")
        print(f"Password: {form.password.data}")

        # Redirect to a success page or perform other actions

    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run()
