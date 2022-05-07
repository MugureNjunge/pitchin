from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired,Length, Email,EqualTo

class SignupForm(FlaskForm):
  username =StringField ('Username', validators= [DataRequired(),Length(min=3, max=12)])
  email = StringField('Email', validators=[DataRequired(), Email])
  password= PasswordField('Password', validators=[DataRequired(), Email])
  confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
  submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email])
  password= PasswordField('Password', validators=[DataRequired(), Email])
  rememeber = BooleanField('Remember Me')
  submit=SubmitField('Log in')



