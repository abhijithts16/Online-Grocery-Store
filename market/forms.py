from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, StringField, PasswordField, SubmitField
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