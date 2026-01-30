from flask import Blueprint, render_template, abort
from app.models import User, Product, Review
from flask_login import login_required, current_user
from sqlalchemy.sql import func

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/dashboard")
@login_required
def dashboard():
    if current_user.role != "admin":
        abort(403)

    total_users = User.query.count()
    total_products = Product.query.count()
    avg_rating = Review.query.with_entities(func.avg(Review.rating)).scalar()

    return render_template("analytics.html",
        total_users=total_users,
        total_products=total_products,
        avg_rating=avg_rating
    )
