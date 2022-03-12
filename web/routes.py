from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("home.html")
