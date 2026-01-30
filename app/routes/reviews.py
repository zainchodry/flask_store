from flask import Blueprint, redirect, url_for, abort
from app.extenshions import db
from app.models import Review, Product
from app.forms import ReviewForm
from flask_login import login_required, current_user

reviews_bp = Blueprint("reviews", __name__)

@reviews_bp.route("/add/<int:product_id>", methods=["GET","POST"])
@login_required
def add_review(product_id):
    if current_user.role != "customer":
        abort(403)

    product = Product.query.get_or_404(product_id)
    form = ReviewForm()

    if form.validate_on_submit():
        review = Review(
            rating=form.rating.data,
            comment=form.comment.data,
            user_id=current_user.id,
            product_id=product.id
        )
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("products.list_products"))
