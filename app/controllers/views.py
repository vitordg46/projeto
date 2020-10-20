from app import suamascara, l_m
from flask_login import login_user
from flask import render_template, redirect, url_for

from app.models.forms import LoginForm, CadastroForm, MascaraForm
from app.models.tables import User, Mascara

@l_m.user_loader
def load_user(id):
  return User.select().filter(id=id)

@suamascara.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@suamascara.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user=User.get(email=form.email.data, password=form.password.data)
    if user and user.password == form.password.data:
      login_user(user)
      return redirect(url_for("catalogo"))
  else: 
    print(form.errors)
  return render_template('login.html', form=form)

@suamascara.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
  form = CadastroForm()
  if form.validate_on_submit():
    
    User.create(name=form.name.data,email=form.email.data,password=form.password.data)
  else:
    print(form.errors)
  return render_template('cadastro.html', form=form)

@suamascara.route('/mascara', methods=['GET','POST'])
def mascara():
  form = MascaraForm()
  if form.validate_on_submit():
    Mascara.create(title=form.title.data, about=form.about.data, price=form.price.data)
  else:
    print(form.errors)
  return render_template('mascara.html', form=form)

@suamascara.route('/catalogo')
def catalogo():
  return render_template('catalogo.html')




