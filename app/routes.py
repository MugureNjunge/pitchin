from flask import render_template, url_for, flash, redirect
from app import app, db 
from app.forms import SignupForm, LoginForm
from app.models import User, Post
from flask_login import login_user, current_user,logout_user, login_required

posts = [
  {
    'title' :'Interview Pitch',
    'content':'Preparing for that important inteview ,gauge just how ready you are. All the very best.'
    
  },
  {
    'title' :'Business Proposal',
    'content':'The investors you have been cozing upto are a pitch away.'
    
  },
  {
    'title' :'Get that groove on!',
    'content':'Going on a date with that special someone ,well lets get you date ready.'
    
  },
  {
    'title' :'Just for fun pitch!',
    'content':'Wamma learn how to make a great pitch in under 60 seconds?Start now and thank me later.'

  }
]

@app.route("/")
def home():
  return render_template("home.html", posts=posts)

@app.route("/about")
def about():
  return render_template("about.html", title = about) 

@app.route("/signup",methods=['GET', 'POST'] )
def signup():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = SignupForm()
  if form.validate_on_submit():
    
    user = User(username=form.username.data, email=form.email.data, password=form.password.data)

    flash('Account created!You can now log in!','success')
    return redirect(url_for('login'))
  return render_template("signup.html", title = 'Signup', form=form)   

@app.route("/login",methods=['GET', 'POST'] )
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home'))

  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    user = User.query.filter_by(password=form.password.data).first()
    login_user(user, remember=form.remember.data)

    return redirect(url_for('home'))

  else: 
    flash('Login unsuccessful.Please check your email and password', 'danger')
    return render_template("login.html", title = 'Login', form=form) 

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('home'))
  
@app.route("/account")
@login_required
def account():
  return render_template("account.html", title = 'Account')
