from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5a833362f6d90268a308cfd3b2dea7ea'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(15),unique=True, nullable=False)
  email = db.Column(db.String(40),unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(180), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return f"Post('{self.title}', '{self.date_posted}', {self.content})"



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


if  __name__ == '__main__':
  app.run(debug=True)