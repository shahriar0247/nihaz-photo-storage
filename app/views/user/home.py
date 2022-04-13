from flask import render_template, redirect
from app import app

@app.route("/")
def slash_route():
    return redirect("/user/home")

@app.route("/user/home")
def user_home_view():
    return render_template("/user/home.html")