from flask import Blueprint, render_template, redirect, url_for, flash
from app.extenshions import db
from app.models import User, Profile
from app.forms import RegisterForm, LoginForm, ProfileForm
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email = form.email.data).first():
            flash("Email already registered", "danger")
            return redirect(url_for("auth.register"))
        
        if form.password.data != form.confirm_password.data:
            flash("Passwords do not match", "danger")
            return redirect(url_for("auth.register"))
        
        if len(form.password.data) < 6:
            flash("Password must be at least 6 characters long", "danger")
            return redirect(url_for("auth.register"))
        
        hash_password = generate_password_hash(form.password.data)
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=hash_password,
            role=form.role.data
        )
        db.session.add(user)
        db.session.commit()

        profile = Profile(user=user)
        db.session.add(profile)
        db.session.commit()

        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@auth_bp.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            # Redirect users to role-specific dashboards
            if user.role == "seller":
                return redirect(url_for("dashboard.seller_dashboard"))
            if user.role == "admin":
                return redirect(url_for("dashboard.admin_dashboard"))
            # default to customer dashboard
            return redirect(url_for("dashboard.customer_dashboard"))
        flash("Invalid credentials")
    return render_template("login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "success")
    return redirect(url_for("auth.login"))


@auth_bp.route("/profile", methods=["GET","POST"])
@login_required
def profile():
    form = ProfileForm(obj=current_user.profile)
    if form.validate_on_submit():
        form.populate_obj(current_user.profile)
        db.session.commit()
        return redirect(url_for("auth.profile"))
    return render_template("profile.html", form=form)
