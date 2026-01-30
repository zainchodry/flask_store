from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, TextAreaField,
    IntegerField, FloatField, SelectField, SubmitField, EmailField
)
from wtforms.validators import DataRequired, Email, Length, NumberRange, EqualTo


class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    role = SelectField(
        "Role",
        choices=[("customer", "Customer"), ("seller", "Seller"), ("admin", "Admin")],
        validators=[DataRequired()]
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class ProfileForm(FlaskForm):
    bio = TextAreaField("Bio")
    phone = StringField("Phone")
    address = TextAreaField("Address")
    submit = SubmitField("Update Profile")


class ProductForm(FlaskForm):
    name = StringField("Product Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    submit = SubmitField("Save Product")


class ReviewForm(FlaskForm):
    rating = IntegerField("Rating (1–5)", validators=[DataRequired(), NumberRange(min=1, max=5)])
    comment = TextAreaField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Review")


class CartForm(FlaskForm):
    quantity = IntegerField("Quantity", validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField("Add to Cart")
