# flask routes
from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from .forms import Add
from .models import Cafe, db


main = Blueprint("main", __name__, template_folder='app/templates')



@main.route("/")
@main.route("/home")
def home():
    cafes = db.session.query(Cafe).all()
    return render_template("index.html", cafes=cafes)

@main.route("/cafe_details/<int:cafe_id>")
def cafe_details(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    return render_template("cafe_details.html", cafe=cafe)



@main.route("/add", methods=["GET", "POST"])
def add():
    form = Add()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name = form.name.data,
            describe = form.describe.data,
            location_url = form.location_url.data,
            bg_url = form.bg_url.data,
            cafe_url = form.cafe_url.data,
            cafe = form.cafe.data,
            wifi = form.wifi.data,
            sockets = form.sockets.data,
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template("add_cafe.html", form=form)

@main.route("/delete/<int:cafe_id>")
def delete(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('main.home'))