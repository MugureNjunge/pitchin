from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import SignupForm, LoginForm
from app.models import User, Post


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
  form = SignupForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!','success')
    return redirect(url_for('home'))
  return render_template("signup.html", title = 'Signup', form=form)   

@app.route("/login",methods=['GET', 'POST'] )
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@g.com' and form.password.data == 'password':
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login unsuccessful.PLease check your email and password', 'danger')

  return render_template("login.html", title = 'Login', form=form)   
