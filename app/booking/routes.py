from app.booking import booking
from flask import render_template,request,url_for,redirect,flash
from app.extensions import db,mail
from app.models import Booking
from flask_login import login_required, current_user
from datetime import date,time,datetime as dt
from flask_mail import Message
import os

@booking.route("/dashboard")
@login_required
def dashboard():
    user_booked = Booking.query.filter_by(user_id = current_user.id).all()
    return render_template("booking/dashboard.html", bookings = user_booked)

@booking.route("/create_booking", methods=["GET","POST"])
@login_required
def create_booking():
    if request.method == "POST":
        service = request.form.get("service")
        if service == "other":
            service = request.form.get("other")
        date_str = request.form.get("date")
        time_str = request.form.get("time")
        date_obj = date.fromisoformat(date_str)
        time_obj = time.fromisoformat(time_str)
        datetime_obj = dt.combine(date_obj,time_obj)
        notes = request.form.get("notes")   
        booking = Booking(service = service, datetime = datetime_obj, notes =notes,user_id = current_user.id)
        db.session.add(booking)
        db.session.commit()
        flash("A new booking has been created","success")
        msg = Message(
            subject=f"Confirmation Email for {current_user.username}",
            recipients=[current_user.email],
        )
        msg.body = f"This email is to confirm you have a booking for {booking.service} and it's due in {booking.datetime}"
        mail.send(msg)
        
        return redirect(url_for("booking.dashboard"))    

    return render_template("booking/create.html")

@booking.route("/cancel/<int:booking_id>")
@login_required
def cancel(booking_id):
    booking = Booking.query.filter_by(id = booking_id ).first()
    db.session.delete(booking)
    db.session.commit()
    return redirect(url_for("booking.dashboard")) 