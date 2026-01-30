from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard/admin")
@login_required
def admin_dashboard():
    if current_user.role != "admin":
        return render_template("unauthorized.html"), 403
    return render_template("admin_dashboard.html")


@dashboard_bp.route("/dashboard/seller")
@login_required
def seller_dashboard():
    if current_user.role != "seller":
        return render_template("unauthorized.html"), 403
    return render_template("seller_dashboard.html")


@dashboard_bp.route("/dashboard/customer")
@login_required
def customer_dashboard():
    return render_template("customer_dashboard.html")
