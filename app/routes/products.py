from flask import Blueprint, render_template, redirect, url_for, abort
from app.extenshions import db
from app.models import Product
from app.forms import ProductForm
from flask_login import login_required, current_user

products_bp = Blueprint("products", __name__)

@products_bp.route("/")
def list_products():
    products = Product.query.all()
    return render_template("products.html", products=products)


@products_bp.route("/add", methods=["GET","POST"])
@login_required
def add_product():
    if current_user.role != "seller":
        abort(403)

    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            seller=current_user
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for("products.list_products"))
    return render_template("product_form.html", form=form)
