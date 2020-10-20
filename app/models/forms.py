from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FloatField, TextField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
  
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])


class CadastroForm(FlaskForm):

  name = StringField('Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])


class MascaraForm(FlaskForm):

  title = StringField('Title', validators=[DataRequired()])
  about = TextField('About', validators=[DataRequired()])
  price = FloatField('Price', validators=[DataRequired()])
