'''Name of file :  resume.py
Author: Jorge Argueta
Date Created: December 16st, 2020
Date Updated: December 16th, 2020
purpose :
        This will make a web page that showcases my resume  '''

from flask import Flask, redirect, url_for, render_template
import os
##starts flask app 
app = Flask(__name__)
PEOPLE_FOLDER = os.path.join('static', 'images')

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/wordpress")
def wordpress():
    return render_template("wordpress.html")


@app.route("/adobe")
def adobe():
    return render_template("adobe_porfolio.html")


@app.route("/gear")
def gear():
    return render_template("gear.html")

@app.route("/reviews")
def reviews():
    return render_template("reviews.html")

if __name__ == "__main__":
    app.run(debug = True)