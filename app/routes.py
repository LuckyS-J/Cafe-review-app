# flask routes
from functools import wraps

from flask import Blueprint, render_template, url_for, flash, abort
from werkzeug.utils import redirect
from app.models import bcrypt, Comment, admin_only
from .forms import Add, Register, Login, CommentForm
from .models import Cafe, db, User, login_manager
from flask_login import login_user, login_required, logout_user, current_user

main = Blueprint("main", __name__, template_folder='app/templates')


@main.route("/")
@main.route("/home")
def home():
    cafes = db.session.query(Cafe).all()
    return render_template("index.html", cafes=cafes, current_user=current_user)

@main.route("/cafe_details/<int:cafe_id>", methods=["GET", "POST"])
def cafe_details(cafe_id):
    form = CommentForm()
    cafe = db.get_or_404(Cafe, cafe_id)
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to be logged to comment.")
            return redirect(url_for("main.login"))
        else:
            new_comment = Comment(
                content=form.comment_text.data,
                author=current_user,
                parent_cafe=cafe,
            )
            db.session.add(new_comment)
            db.session.commit()
    return render_template("cafe_details.html", cafe=cafe, current_user=current_user, form=form)

@main.route("/add", methods=["GET", "POST"])
@login_required
@admin_only
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
    return render_template("add_cafe.html", form=form, current_user=current_user)

@main.route("/delete/<int:cafe_id>")
@login_required
@admin_only
def delete(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('main.home'))

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        email = form.email.data
        user =  db.session.query(User).filter_by(email=email).first()
        if not user:
            new_user = User(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=bcrypt.generate_password_hash(f"{form.password.data}").decode('utf-8'),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('main.home'))
        else:
            flash("Wrong email. User already exist")
    return render_template("register.html", form=form, current_user=current_user)

@main.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                flash("Successfully logged in!")
                return redirect(url_for('main.home'))
            else:
                flash("Wrong password")
        else:
            flash("Wrong email")
    return render_template("login.html", form=form)

@main.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("Successfully logged out!")
    return redirect(url_for('main.home'))