from http.client import HTTPResponse
import os
from xml.dom.expatbuilder import FragmentBuilder
from flask import flash, redirect, render_template, request, url_for, session
from pyparsing import nums
from market import app, db, bcrypt
import random
from datetime import datetime,date
from functools import wraps
from markupsafe import escape
from market.forms import AddProductForm, CustomerRegistrationForm, AdminRegistrationForm, DeliveryBoyForm, OrderForm, SellerProductForm, SellerRegistrationForm, LoginForm, PromoOfferForm, PromoCodeForm
from werkzeug.utils import secure_filename
from .models import Customer, Admin, Seller, Order, Offer, DeliveryBoy, Product, Cart, AssociatedWith, Sells

cart_id=0
total_val=0.0
total_count=0.0
customer_cart_list=[]

UPLOAD_FOLDER = 'market/static/uploads' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def auth_required(role=None):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Check if the user is logged in
            if 'user_id' not in session:
                flash('You need to log in first.')
                return render_template('homepage.html')

            # Check the user's role
            if role and session.get('user_type') != role:
                flash('You do not have permission to access this page.')
                return render_template('homepage.html')

            # Check if the user_id in session matches any of the expected IDs in kwargs
            if ('user_id' in kwargs and session['user_id'] != int(kwargs['user_id'])) or \
               ('seller_id' in kwargs and session['user_id'] != int(kwargs['seller_id'])) or \
               ('admin_id' in kwargs and session['user_id'] != int(kwargs['admin_id'])):
                flash('Unauthorized access. Please log in to continue!')
                return render_template('homepage.html')

            return f(*args, **kwargs)
        return decorated_function
    return wrapper

@app.route('/admin/<admin_id>')
@auth_required('admin')
def adminRedirect(admin_id):
    return render_template('adminOption.html', admin_id=admin_id)

@app.route('/adminOrder/<admin_id>', methods=['GET', 'POST'])
@auth_required('admin')
def adminViewOrder(admin_id):
    my_list = []
    order_all = Order.query.all()
    for order in order_all:
        temp_dict = {
            'Order_ID': order.order_id,
            'Mode': order.mode,
            'Amount': order.amount,
            'Date': order.date
        }
        my_list.append(temp_dict)
    if request.method == 'POST':
        return redirect('/admin/' + str(admin_id))
    return render_template('viewOrder.html', list=my_list)

@app.route('/adminOffer/<admin_id>', methods=['GET', 'POST'])
@auth_required('admin')
def adminAddOffer(admin_id):
    form = PromoOfferForm()
    if form.validate_on_submit():
        promo_code = form.promo_code.data
        percentage_discount = form.percentage_discount.data
        min_ordervalue = form.min_ordervalue.data
        max_discount = form.max_discount.data
        new_offer = Offer(
            promo_code=promo_code,
            percentage_discount=percentage_discount,
            min_ordervalue=min_ordervalue,
            max_discount=max_discount,
            admin_id=admin_id
        )
        db.session.add(new_offer)
        db.session.commit()
        flash('You have successfully added an Offer!')
        return redirect(url_for('adminAddOffer', admin_id=admin_id))
    return render_template('addOffer.html', admin_id=admin_id, form=form)

@app.route('/adminDelivery_boy/<admin_id>', methods=['GET', 'POST'])
@auth_required('admin')
def adminAdd_Delivery_Boy(admin_id):
    form = DeliveryBoyForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        mobile_no = form.mobile_no.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_delivery_boy = DeliveryBoy(
            first_name=first_name,
            last_name=last_name,
            mobile_no=mobile_no,
            email=email,
            password=hashed_password,
            admin_id=admin_id
        )
        db.session.add(new_delivery_boy)
        db.session.commit()
        flash('You have successfully added a delivery boy!')
        return redirect(url_for('adminAdd_Delivery_Boy', admin_id=admin_id))
    return render_template('addDelivery.html', form=form, admin_id=admin_id)

@app.route('/adminSeller/<admin_id>', methods=['GET', 'POST'])
@auth_required('admin')
def adminAdd_Seller(admin_id):
    form = SellerRegistrationForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        phone_number = form.phone_number.data
        password = form.password.data
        place_of_operation = form.place_of_operation.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_seller = Seller(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=hashed_password,
            place_of_operation=place_of_operation,
            admin_id=admin_id
        )
        db.session.add(new_seller)
        db.session.commit()
        flash('You have successfully added a seller!')
        return redirect(url_for('adminAdd_Seller', admin_id=admin_id))
    return render_template('addSeller.html', admin_id=admin_id, form=form)

@app.route('/adminProduct/<admin_id>', methods=['GET', 'POST'])
@auth_required('admin')
def adminAdd_Product(admin_id):
    form = AddProductForm()
    if form.validate_on_submit():

        # Save the uploaded image 
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        image_file = form.image.data 
        filename = secure_filename(image_file.filename) 
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename) 
        image_file.save(image_path)
        
        # Create a new product object
        new_product = Product(
        name=form.name.data,
        price=form.price.data,
        brand=form.brand.data,
        measurement=form.measurement.data,
        category_id=form.category_id.data,
        unit=form.unit.data,
        admin_id=admin_id,
        image=filename
        )
            
        # Add to the session and commit to the database
        db.session.add(new_product)
        db.session.commit()
        flash('You have successfully added a Product!', 'success')
        return redirect(url_for('adminAdd_Product', admin_id=admin_id))
    return render_template('addNewProducts.html', admin_id=admin_id, form=form)

@app.route('/sell/<seller_id>', methods=['GET', 'POST'])
@auth_required('seller')
def sell(seller_id):
    form = SellerProductForm()
    if form.validate_on_submit():
        name = form.name.data
        brand = form.brand.data
        quantity = form.quantity.data
        product = Product.query.filter_by(name=name, brand=brand).first()
        if not product or quantity < 0:
            flash('Invalid Product details or Quantity')
        else:
            new_sale = Sells(Seller_ID=seller_id, Product_ID=product.Product_ID, No_of_Product_Sold=quantity)
            db.session.add(new_sale)
            db.session.commit()
            flash('Product added successfully')
        return redirect(url_for('sell', seller_id=seller_id))
    return render_template('addProduct.html', form=form)

def reinitialize():
    global cart_id
    global total_count
    global total_val
    global customer_cart_list
    cart_id = StaticClass.giveCartId()
    total_val=0.0
    total_count=0.0
    customer_cart_list=[]

@app.route('/home/<user_id>', methods=['GET', 'POST'])
@auth_required('customer')
def userEnter(user_id):
    my_list = []
    global cart_id, total_count, total_val, customer_cart_list
    products = Product.query.all()
    for prod in products:
        temp_dict = {
            'Name': prod.name,
            'Price': prod.price,
            'Brand': prod.brand,
            'Image': prod.image or 'default.png'  # Use 'default.png' if no image is uploaded
        }
        my_list.append(temp_dict)
    if request.method == 'POST':
        new_cart = Cart(Cart_ID=cart_id, Total_Value=total_val, Total_Count=total_count, Offer_ID=3, Final_Amount=total_val)
        db.session.add(new_cart)
        db.session.commit()
        return redirect(url_for('placeOrder', user_id=user_id))
    else:
        purchaseDetails = request.args
        if 'Name' in purchaseDetails and 'Brand' in purchaseDetails and 'Price' in purchaseDetails:
            try:
                name = purchaseDetails['Name']
                brand = purchaseDetails['Brand']
                price = purchaseDetails['Price']
                total_count += 1
                total_val += float(price)
                temp_dict = {'Name': name, 'Brand': brand, 'Price': price}
                customer_cart_list.append(temp_dict)
                flash('Product has been added successfully to the cart!')
            except KeyError:
                flash("Error: KeyError")

    return render_template('home.html', list=my_list)


@app.route('/remove_from_cart/<int:user_id>/<item_name>', methods=['POST'])
@auth_required('customer')
def remove_from_cart(user_id, item_name):
    global customer_cart_list, total_val, cart_id

    # Remove item from global cart list
    for item in customer_cart_list:
        if item['Name'] == item_name:
            total_val -= float(item['Price'])
            customer_cart_list.remove(item)
            break

    # Update the cart in the database
    cart = Cart.query.filter_by(Cart_ID=cart_id).first()
    if cart:
        cart.Total_Value = total_val
        cart.Total_Count = len(customer_cart_list)
        cart.Final_Amount = total_val  # Assuming Final_Amount equals Total_Value without discount
        db.session.commit()

    flash(f'{item_name} has been removed from your cart.')
    return redirect(url_for('placeOrder', user_id=user_id))

@app.route('/order/<user_id>', methods=['GET', 'POST'])
@auth_required('customer')
def placeOrder(user_id):
    global customer_cart_list, cart_id, total_val
    form = PromoCodeForm()
    if form.validate_on_submit():
        p_code = form.promo_code.data
        offer = Offer.query.filter_by(promo_code=p_code).first()
        if not offer or p_code == 'Coupon_Code':
            new_cart_offer = Cart.query.filter_by(Cart_ID=cart_id).first()
            new_cart_offer.Offer_ID = None
            db.session.commit()
        else:
            if total_val > offer.min_ordervalue:
                dval = (total_val * offer.percentage_discount) / 100
                deduct = min(dval, offer.max_discount)
                total_val -= deduct
                new_cart_offer = Cart.query.filter_by(Cart_ID=cart_id).first()
                new_cart_offer.Offer_ID = offer.Offer_ID
                new_cart_offer.Final_Amount = total_val
                db.session.commit()
        for item in customer_cart_list:
            product = Product.query.filter_by(name=item['Name']).first()
            if product:
                new_association = AssociatedWith(Customer_ID=user_id, Cart_ID=cart_id, Product_ID=product.Product_ID)
                db.session.add(new_association)
                db.session.commit()
        return redirect(url_for('order_placing', user_id=user_id))
    for item in customer_cart_list:
        product = Product.query.filter_by(name=item['Name']).first()
        if product:
            if product.image and product.image != 'None':
                image_path = 'uploads/' + product.image
            else:
                image_path = 'uploads/default.png'
            item['Image'] = image_path
        else:
            item['Image'] = 'uploads/default.png'
    return render_template('order.html', list=customer_cart_list, form=form, total_val=total_val, user_id=user_id) # Pass the form to the template

@app.route('/HomePage')
@app.route('/')
def homePage():
    return render_template('homepage.html')

@app.route('/loginRegisterSeller')
def loginRegisterSeller():
    return render_template('loginregisterSeller.html')

@app.route('/loginRegisterUser')
def loginRegisterUser():
    return render_template('loginregisterUser.html')

@app.route('/loginRegisterAdmin')
def loginRegisterAdmin():
    return render_template('loginregisterAdmin.html')

@app.route('/placeOrder/<user_id>', methods=['GET', 'POST'])
@auth_required('customer')
def order_placing(user_id):
    global total_val, cart_id
    form = OrderForm()
    if form.validate_on_submit():
        hno = form.hno.data
        city = form.city.data
        state = form.state.data
        pincode = form.pincode.data
        mode = form.mode.data
        curr_date = datetime.today().strftime('%Y-%m-%d')
        current_time = datetime.now().strftime("%H:%M:%S")
        delivery_boy_ids = [boy.Delivery_Boy_ID for boy in DeliveryBoy.query.all()]
        delivery_boy_id = random.choice(delivery_boy_ids) if delivery_boy_ids else None
        new_order = Order(
            mode=mode,
            amount=total_val,
            city=city,
            state=state,
            date=curr_date,
            house_flat_no=hno,
            pincode=pincode,
            cart_id=cart_id,
            delivery_boy_id=delivery_boy_id,
            order_time=current_time
        )
        db.session.add(new_order)
        db.session.commit()
        flash('Your Order has been placed Successfully!')
        url_direct = '/home/' + str(user_id)
        return redirect(url_direct)
    return render_template('orderDetails.html', total_val=total_val, form=form)


@app.route('/customerRegister', methods=['GET', 'POST'])
def customerRegister():
    form = CustomerRegistrationForm()
    if form.validate_on_submit():
        first_name = escape(form.first_name.data)
        last_name = escape(form.last_name.data)
        email = escape(form.email.data)
        mobile_no = escape(form.mobile_no.data)
        password = form.password.data
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        # Create a new customer
        new_customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile_no=mobile_no,
            password=hashed_password
        )
        # Add the new customer to the session and commit to the database
        db.session.add(new_customer)
        db.session.commit()
        flash('You have registered successfully!')
        return redirect(url_for('UserLogin'))
    return render_template('customerRegister.html', form=form)

@app.route('/adminRegister', methods=['GET', 'POST'])
def adminRegister():
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        first_name = escape(form.first_name.data)
        last_name = escape(form.last_name.data)
        password = form.password.data
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        # Create a new admin
        new_admin = Admin(
            first_name=first_name,
            last_name=last_name,
            password=hashed_password
        )
        # Add the new admin to the session and commit to the database
        db.session.add(new_admin)
        db.session.commit()
        flash('You have registered successfully!')
        return redirect(url_for('AdminLogin'))
    return render_template('adminRegister.html', form=form)

@app.route('/sellerRegister', methods=['GET', 'POST'])
def sellerRegister():
    form = SellerRegistrationForm()
    if form.validate_on_submit():
        first_name = escape(form.first_name.data)
        last_name = escape(form.last_name.data)
        email = escape(form.email.data)
        password = form.password.data
        phone_number = escape(form.phone_number.data)
        place_of_operation = escape(form.place_of_operation.data)
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        # Select a random admin ID
        rand_admin = db.session.execute('SELECT Admin_ID FROM admin').fetchall()
        admin_id = random.choice(rand_admin)[0] if rand_admin else None
        # Create a new seller
        new_seller = Seller(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=hashed_password,
            place_of_operation=place_of_operation,
            admin_id=admin_id
        )
        # Add the new seller to the session and commit to the database
        db.session.add(new_seller)
        db.session.commit()
        flash('You have registered successfully!')
        return redirect(url_for('SellerLogin'))
    return render_template('sellerRegister.html', form=form)

@app.route('/UserLogin', methods=['GET', 'POST'])
def UserLogin():
    form = LoginForm()
    if form.validate_on_submit():
        email = escape(form.email.data)
        password = form.password.data
        # Fetch the user by email
        customer = Customer.query.filter_by(email=email).first()
        if customer and bcrypt.check_password_hash(customer.password, password):
            session['user_id'] = customer.Customer_ID
            session['user_type'] = 'customer'
            session.permanent = True
            reinitialize()
            url_direct = '/home/' + str(customer.Customer_ID)
            return redirect(url_direct)
        else:
            flash('Invalid Email or Password')
    return render_template('UserLogin.html', form=form)

from market.forms import CustomerRegistrationForm, AdminRegistrationForm, SellerRegistrationForm, LoginForm, AdminLoginForm

@app.route('/AdminLogin', methods=['GET', 'POST'])
def AdminLogin():
    form = AdminLoginForm()
    if form.validate_on_submit():
        first_name = escape(form.first_name.data)
        last_name = escape(form.last_name.data)
        password = form.password.data
        # Fetch the admin by name
        admin = Admin.query.filter_by(first_name=first_name, last_name=last_name).first()
        if admin and bcrypt.check_password_hash(admin.password, password):
            session['user_id'] = admin.Admin_ID
            session['user_type'] = 'admin'
            session.permanent = True
            url_direct = '/admin/' + str(admin.Admin_ID)
            return redirect(url_direct)
        else:
            flash('Invalid Name or Password')
    return render_template('AdminLogin.html', form=form)

@app.route('/SellerLogin', methods=['GET', 'POST'])
def SellerLogin():
    form = LoginForm()
    if form.validate_on_submit():
        email = escape(form.email.data)
        password = form.password.data
        # Fetch the seller by email
        seller = Seller.query.filter_by(email=email).first()
        if seller and bcrypt.check_password_hash(seller.password, password):
            session['user_id'] = seller.Seller_ID
            session['user_type'] = 'seller'
            session.permanent = True
            url_direct = '/sell/' + str(seller.Seller_ID)
            return redirect(url_direct)
        else:
            flash('Invalid Email or Password')
    return render_template('SellerLogin.html', form=form)

class StaticClass:
    
    cart_id = random.randint(1000,100000)

    @staticmethod
    def giveCartId():
        StaticClass.cart_id +=1
        return StaticClass.cart_id