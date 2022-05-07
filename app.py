from flask import Flask, render_template, url_for, flash, redirect
from forms import (SignupForm, LoginForm)
app = Flask(__name__)

app.config['SECRET_KEY'] = '567ygh345gbn9765klm2'

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
    flash(f'Welcome {form.username.data}!','Your account has been successfully created. Add your own post now!')
    return redirect(url_for('home'))
  return render_template("signup.html", title = 'Signup', form=form)   

@app.route("/login")
def login():
  form = LoginForm()
  return render_template("login.html", title = 'Login', form=form)   


if  __name__ == '__main__':
  app.run(debug=True)