#getting some basics on using flask for web development 
#route mapping, page functions, redirects
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the main page. <h1>HELLO!<h1>"

@app.route("/<name>")
def user(name):
    #passing a list to index page
    return render_template("index.html", content=["Tim","Joe","Bill"])

if __name__== "__main__":
    app.run()



""" @app.route("/admin")
def admin():
    return redirect(url_for("home")) """