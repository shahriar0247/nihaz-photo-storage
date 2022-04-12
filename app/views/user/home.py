from flask import render_template
from app import app

@app.route("/user/home")
def user_home_view():
    return render_template("/user/home.html")