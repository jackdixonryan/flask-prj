# Imports flask and render template
from flask import Flask, render_template, flash, redirect, url_for
from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Odso2i3iue4b65ios7akwkjg438vdyuf046'

# Got some server side data here, nothing too fancy.
posts = [
  {
    "author": "Jack Ryan",
    "title": "Using Flask",
    "content": "Using flask is very easy! Get a server up and running in seconds! Huzzah.",
    "date_posted": "12/15/2018"
  }
]

# these two routes render the static html file in our templates directory passing posts in to the template.
@app.route("/")
@app.route("/home")
def home():
  return render_template("index.html", posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash('Account created for %s!' %(form.username.data), 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title="Register", form=form)

@app.route("/login")
def login():
  form = LoginForm()
  return render_template('login.html', title="Login", form=form)