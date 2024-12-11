from flask_wtf import FlaskForm
from wtforms import DecimalField, FloatField, IntegerField, SelectField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp, NumberRange
import re
from flask_wtf.file import FileField, FileRequired, FileAllowed

# Custom validator for password complexity
def validate_password(form, field):
    password = field.data
    if len(password) < 8 or len(password) > 20:
        raise ValidationError('Password must be between 8 and 20 characters long.')
    if not re.search(r'[A-Za-z]', password):
        raise ValidationError('Password must contain at least one letter.')
    if not re.search(r'\d', password):
        raise ValidationError('Password must contain at least one number.')
    if re.search(r'[ \t\n\r\f\v]', password):
        raise ValidationError('Password must not contain spaces.')
    if re.search(r'[^A-Za-z0-9]', password):
        raise ValidationError('Password must not contain special characters or emoji.')

class CustomerRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mobile_no = StringField('Mobile No', validators=[DataRequired(), Length(min=10, max=10), Regexp(r'^\d{10}$', message="Phone number must contain only digits.")])
    password = PasswordField('Password', validators=[DataRequired(), validate_password])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class AdminRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), validate_password])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class SellerRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Mobile No', validators=[DataRequired(), Length(min=10, max=10), Regexp(r'^\d{10}$', message="Phone number must contain only digits.")])
    place_of_operation = StringField('Place Of Operation', validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField('Password', validators=[DataRequired(), validate_password])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AdminLoginForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AddProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)])
    brand = StringField('Brand', validators=[DataRequired(), Length(min=1, max=100)])
    measurement = StringField('Measurement', validators=[DataRequired(), Length(min=1, max=100)])
    category_id = IntegerField('Category ID', validators=[DataRequired()])
    unit = StringField('Unit', validators=[DataRequired(), Length(min=1, max=100)])
    image = FileField('Product Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!'), FileRequired()])
    submit = SubmitField('Add Product')

class PromoOfferForm(FlaskForm):
    promo_code = StringField('Promo Code', validators=[DataRequired(), Length(min=2, max=20)])
    percentage_discount = DecimalField('Percentage Discount', validators=[DataRequired(), NumberRange(min=0, max=100, message="Percentage must be between 0 and 100")])
    min_ordervalue = DecimalField('Minimum Order Value', validators=[DataRequired(), NumberRange(min=0, message="Order value must be positive")])
    max_discount = DecimalField('Maximum Discount', validators=[DataRequired(), NumberRange(min=0, message="Discount must be positive")])
    submit = SubmitField('Add Offer')

class PromoCodeForm(FlaskForm): 
    promo_code = StringField('Promo Code', default='Coupon_Code', validators=[DataRequired()])
    submit = SubmitField('Place Order')

class OrderForm(FlaskForm): 
    hno = StringField('House Number', validators=[DataRequired(), Length(min=1, max=100)]) 
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=100)]) 
    state = StringField('State', validators=[DataRequired(), Length(min=2, max=100)]) 
    pincode = StringField('Pincode', validators=[DataRequired(), Length(min=6, max=6), Regexp(r'^\d{6}$', message="Pincode must be exactly 6 digits.")]) 
    mode = SelectField('Payment Mode', choices=[('Cash', 'Cash'), ('Card', 'Card'), ('UPI', 'UPI')], validators=[DataRequired()]) 
    submit = SubmitField('Place Order')

class DeliveryBoyForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    mobile_no = StringField('Mobile Number', validators=[DataRequired(), Regexp(r'^\d{10}$', message="Mobile number must be 10 digits.")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Add Delivery Boy')

def validate_percentage_discount(form, field):
    if field.data <= 0 or field.data > 100:
        raise ValidationError('Percentage discount must be between 0 and 100.')

class PromoOfferForm(FlaskForm):
    promo_code = StringField('Promo Code', validators=[DataRequired(), Length(min=3, max=50)])
    percentage_discount = FloatField('Percentage Discount', validators=[DataRequired(), validate_percentage_discount])
    min_ordervalue = FloatField('Min Order Value', validators=[DataRequired(), NumberRange(min=0)])
    max_discount = FloatField('Maximum Discount', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Add Offer')

class SellerProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired(), Length(min=2, max=100)])
    brand = StringField('Brand', validators=[DataRequired(), Length(min=2, max=100)])
    quantity = IntegerField('Quantity to Add', validators=[DataRequired(), NumberRange(min=1, message="Quantity must be at least 1")])
    submit = SubmitField('Submit')
