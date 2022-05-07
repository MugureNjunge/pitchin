from flask import Flask,render_template,url_for
app = Flask(__name__)

posts = [
  {
    
    'content':'Preparing for that important inteview - lets gauge just how ready you are!',
    'title' :'Interview Pitch'
  },
  {
    'content':'The investors you have been cozing upto are a pitch away!',
    'title' :'Business Proposal'

  },
  {
    'content':'Going on a date with that special someone - well lets get you date ready!',
    'title' :'Date PItch'
  }
]

@app.route("/")
def home():
  return render_template("home.html", posts=posts)

@app.route("/about")
def about():
  return render_template("about.html", title = about) 

if  __name__ == '__main__':
  app.run(debug=True)