# Flask Store

A comprehensive multi-user e-commerce platform built with Flask, featuring user authentication, product management, order processing, and analytics dashboards.

## 🚀 Features

- **User Authentication**: User registration and login with role-based access control
- **Multiple User Roles**: Admin, Seller, and Customer roles with distinct permissions
- **Product Management**: Sellers can create, update, and manage their products
- **Product Reviews**: Customers can rate and review products
- **Order Management**: Full order lifecycle management with status tracking
- **Shopping Analytics**: Track sales, revenue, and customer insights
- **User Dashboards**: Role-specific dashboards for admin, sellers, and customers
- **User Profiles**: Customers and sellers can manage their profiles
- **Responsive Design**: Modern, responsive UI with CSS styling

## 📋 Project Structure

```
flask_store/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── extenshions.py        # Flask extensions (SQLAlchemy, Login Manager)
│   ├── models.py             # Database models
│   ├── forms.py              # WTForms for form validation
│   ├── routes/               # Blueprint route handlers
│   │   ├── auth.py           # Authentication routes (login, register, logout)
│   │   ├── dashboard.py      # Dashboard routes for different user roles
│   │   ├── products.py       # Product management routes
│   │   ├── reviews.py        # Review management routes
│   │   ├── orders.py         # Order management routes
│   │   └── analytics.py      # Analytics and statistics routes
│   ├── static/               # Static files (CSS, JavaScript, images)
│   │   └── css/
│   │       └── style.css     # Main stylesheet
│   └── templates/            # Jinja2 HTML templates
│       ├── base.html         # Base template with navigation
│       ├── login.html        # Login page
│       ├── register.html     # Registration page
│       ├── profile.html      # User profile page
│       ├── products.html     # Product listing page
│       ├── product_form.html # Product creation/edit form
│       ├── reviews.html      # Product reviews page
│       ├── orders.html       # Orders listing page
│       ├── analytics.html    # Analytics dashboard
│       ├── admin_dashboard.html     # Admin dashboard
│       ├── seller_dashboard.html    # Seller dashboard
│       ├── customer_dashboard.html  # Customer dashboard
│       └── unauthorized.html # Access denied page
├── instance/                 # Instance folder (local config, database)
├── config.py                 # Application configuration
├── run.py                    # Application entry point
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## 🗄️ Database Models

### User

- `id` (Primary Key)
- `email` (Unique)
- `username`
- `password` (Hashed)
- `role` (Admin, Seller, Customer)
- Relationships: `profile`, `products`

### Profile

- `id` (Primary Key)
- `bio`
- `phone`
- `address`
- `user_id` (Foreign Key)

### Product

- `id` (Primary Key)
- `name`
- `description`
- `price`
- `seller_id` (Foreign Key to User)
- Relationships: `reviews`

### Review

- `id` (Primary Key)
- `rating` (1-5)
- `comment`
- `product_id` (Foreign Key)
- `user_id` (Foreign Key)

### Order

- `id` (Primary Key)
- `status` (pending, processing, shipped, delivered, canceled)
- `total` (Order total amount)
- `customer_id` (Foreign Key)
- Relationships: `items`

### OrderItem

- `id` (Primary Key)
- `quantity`
- `price` (Unit price at order time)
- `product_id` (Foreign Key)
- `order_id` (Foreign Key)

## 🛠️ Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLAlchemy with SQLite (default) or PostgreSQL
- **Authentication**: Flask-Login for user session management
- **Forms**: WTForms for form validation
- **Frontend**: HTML, CSS, Jinja2 templates
- **Database ORM**: SQLAlchemy

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**

   ```bash
   git clone flask_store.git
   cd flask_store
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:

   ```
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///flask.db
   FLASK_ENV=development
   ```

5. **Initialize the database**

   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

6. **Run the application**
   ```bash
   python run.py
   ```
   The application will be available at `http://localhost:5000`

## 🔐 User Roles & Permissions

### Admin

- View all users and their activities
- Access admin dashboard
- View global analytics
- Manage platform settings

### Seller

- Manage own products (CRUD operations)
- View orders for their products
- Access seller dashboard
- Track sales and revenue

### Customer

- Browse all products
- Add products to cart and place orders
- Write and manage reviews
- Track order status
- Access customer dashboard

## 🔄 Key Routes

### Authentication

- `GET /login` - Login page
- `POST /login` - Process login
- `GET /register` - Registration page
- `POST /register` - Create new account
- `GET /logout` - Logout user

### Products

- `GET /products` - List all products
- `GET /products/new` - Create product form (Seller only)
- `POST /products` - Submit new product (Seller only)
- `GET /products/<id>/edit` - Edit product form (Seller only)
- `POST /products/<id>` - Update product (Seller only)
- `DELETE /products/<id>` - Delete product (Seller only)

### Orders

- `GET /orders` - List user's orders
- `GET /orders/new` - Create new order
- `POST /orders` - Submit order
- `GET /orders/<id>` - Order details

### Reviews

- `GET /products/<id>/reviews` - List product reviews
- `POST /reviews` - Submit review
- `DELETE /reviews/<id>` - Delete review (Author only)

### Dashboards

- `GET /admin` - Admin dashboard
- `GET /seller` - Seller dashboard
- `GET /customer` - Customer dashboard

### Analytics

- `GET /analytics` - View analytics and statistics

## 📝 Configuration

Edit `config.py` to customize:

- `SECRET_KEY` - Flask session encryption key
- `SQLALCHEMY_DATABASE_URI` - Database connection string
- `SQLALCHEMY_TRACK_MODIFICATIONS` - SQLAlchemy tracking flag

## 🧪 Testing

```bash
# Run tests (if test suite exists)
pytest
```

## 🐛 Troubleshooting

### Database Issues

- Delete `instance/flask.db` to reset the database
- Recreate using the initialization steps above

### Module Not Found

- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

### Port Already in Use

- Modify the port in `run.py`: `app.run(debug=True, port=5001)`

## 📦 Dependencies

Main dependencies (see `requirements.txt`):

- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- WTForms
- Werkzeug (for password hashing)

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Commit with clear messages
4. Push to the repository
5. Create a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 📧 Support

For issues or questions, please create an issue in the repository or contact the development team.

---

**Happy Coding! 🎉**
