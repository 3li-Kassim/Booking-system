from flask import flash,request,url_for,render_template,redirect
from app.extensions import db,bcrypt
from app.models import User,Booking
from flask_login import login_required,current_user
from app.admin import admin
from functools import wraps

def admin_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if current_user.role != "admin":
            return redirect(url_for("booking.dashboard"))
        return func(*args,**kwargs)
    return wrapper



@admin.route("/dashboard")
@login_required
@admin_required
def admin_page():
    users = User.query.all()
    all_booking = Booking.query.all()
    return render_template("admin/admin_dashboard.html" ,bookings = all_booking, users = users)