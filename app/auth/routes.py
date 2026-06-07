from app.models import User
from app.extensions import db,bcrypt
from flask import render_template,redirect,request,url_for,flash
from app.auth import auth
from flask_login import login_user, logout_user




@auth.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        existing_user = User.query.filter_by(username= username,email=email).first()
        if not existing_user:
            password = bcrypt.generate_password_hash(password)            
            user = User(username= username, email=email,password=password)
            db.session.add(user)
            db.session.commit()
            flash("account created", "success")
            return redirect(url_for("auth.login"))
        else:
            flash("Account already exists", "danger")

    return render_template("auth/register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()
        if user:
            password = request.form.get("password")
            if bcrypt.check_password_hash(user.password,password):
                login_user(user)
                return redirect(url_for("booking.dashboard"))
            else:
                flash("Wrong password", "danger")
                return redirect(url_for("auth.login"))
        else:
            flash("Account doesn't exist")
            return redirect(url_for("auth.register"))

    return render_template("auth/login.html")


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))