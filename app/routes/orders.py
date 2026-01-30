from flask import Blueprint, render_template, redirect, url_for, abort
from app.extenshions import db
from app.models import Order, OrderItem, Product
from flask_login import login_required, current_user

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/add/<int:product_id>")
@login_required
def add_to_cart(product_id):
    if current_user.role != "customer":
        abort(403)

    product = Product.query.get_or_404(product_id)
    order = Order.query.filter_by(customer_id=current_user.id, status="pending").first()

    if not order:
        order = Order(customer_id=current_user.id)
        db.session.add(order)
        db.session.commit()

    item = OrderItem.query.filter_by(order_id=order.id, product_id=product.id).first()
    if item:
        item.quantity += 1
    else:
        item = OrderItem(order_id=order.id, product_id=product.id, price=product.price, quantity=1)

    db.session.add(item)
    db.session.commit()
    return redirect(url_for("orders.cart"))


@orders_bp.route("/cart")
@login_required
def cart():
    order = Order.query.filter_by(customer_id=current_user.id, status="pending").first()
    return render_template("cart.html", order=order)


@orders_bp.route("/checkout")
@login_required
def checkout():
    order = Order.query.filter_by(customer_id=current_user.id, status="pending").first()
    total = sum(i.quantity * i.price for i in order.items)
    order.total = total
    order.status = "shipped"
    db.session.commit()
    return render_template("checkout.html", order=order)
