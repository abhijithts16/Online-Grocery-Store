from datetime import datetime
from . import db

class Customer(db.Model):
    __tablename__ = 'customer'
    Customer_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    mobile_no = db.Column(db.String(20))
    password = db.Column(db.String(80))

class Admin(db.Model):
    __tablename__ = 'admin'
    Admin_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(80))

class Seller(db.Model):
    __tablename__ = 'seller'
    Seller_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    phone_number = db.Column(db.String(20))
    password = db.Column(db.String(80))
    place_of_operation = db.Column(db.String(100))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.Admin_ID'))

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mode = db.Column(db.String(10), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    house_flat_no = db.Column(db.String(10), nullable=False)
    pincode = db.Column(db.String(6), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.Cart_ID'), nullable=False)
    delivery_boy_id = db.Column(db.Integer, db.ForeignKey('delivery_boy.Delivery_Boy_ID'), nullable=True)
    order_time = db.Column(db.String(50), nullable=False)

class Offer(db.Model):
    __tablename__ = 'offer'
    Offer_ID = db.Column(db.Integer, primary_key=True)
    promo_code = db.Column(db.String(50), unique=True)
    percentage_discount = db.Column(db.Float)
    min_ordervalue = db.Column(db.Float)
    max_discount = db.Column(db.Float)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.Admin_ID'))

class DeliveryBoy(db.Model):
    __tablename__ = 'delivery_boy'
    Delivery_Boy_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    mobile_no = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(80))
    average_rating = db.Column(db.Float, default=None)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.Admin_ID'))

class Product(db.Model):
    __tablename__ = 'product'
    Product_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    brand = db.Column(db.String(100))
    measurement = db.Column(db.String(100))
    category_id = db.Column(db.Integer)
    unit = db.Column(db.String(50))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.Admin_ID'))
    image = db.Column(db.String(120))

class Cart(db.Model):
    __tablename__ = 'cart'
    Cart_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Total_Value = db.Column(db.Float, nullable=False)
    Total_Count = db.Column(db.Integer, nullable=False)
    Offer_ID = db.Column(db.Integer, nullable=True)
    Final_Amount = db.Column(db.Float, nullable=False)

class AssociatedWith(db.Model):
    __tablename__ = 'associated_with'
    id = db.Column(db.Integer, primary_key=True)
    Customer_ID = db.Column(db.Integer, db.ForeignKey('customer.Customer_ID'))
    Cart_ID = db.Column(db.Integer, db.ForeignKey('cart.Cart_ID'))
    Product_ID = db.Column(db.Integer, db.ForeignKey('product.Product_ID'))

class Sells(db.Model):
    __tablename__ = 'sells'
    id = db.Column(db.Integer, primary_key=True)
    Seller_ID = db.Column(db.Integer, db.ForeignKey('seller.Seller_ID'))
    Product_ID = db.Column(db.Integer, db.ForeignKey('product.Product_ID'))
    No_of_Product_Sold = db.Column(db.Integer)

class AuditLog(db.Model):
    __tablename__ = 'audit_log'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    user_type = db.Column(db.String(50), nullable=False)
    action = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
