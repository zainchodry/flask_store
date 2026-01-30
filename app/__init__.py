from flask import Flask
from app.models import User
from config import Config
from flask_login import current_user
from app.extenshions import db, login_manager, migrate
import os

def create_app():
    # Use the package's templates directory (app/templates)
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    from app.routes.auth import auth_bp
    from app.routes.products import products_bp
    from app.routes.orders import orders_bp 
    from app.routes.dashboard import dashboard_bp
    from app.routes.analytics import analytics_bp
    from app.routes.reviews import reviews_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(orders_bp, url_prefix="/orders")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(analytics_bp, url_prefix="/analytics")
    app.register_blueprint(reviews_bp, url_prefix="/reviews")

    with app.app_context():
        db.create_all()
    return app