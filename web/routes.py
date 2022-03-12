from flask import Blueprint, render_template

from web.forms import GetUserDay

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    name = None
    bday = None
    form = GetUserDay()
    
    if form.validate_on_submit():
        name = form.name.data
        bday = form.bday.data
        db.session.commit()

    return render_template("index.html", form=form)

@main.route("/home/")
def home():
    return render_template("home.html")
