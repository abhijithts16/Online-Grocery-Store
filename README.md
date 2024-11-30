# GroStop- An E-Commerce Grocery Store website using Flask
We have incorporated the database in the form of an application
where we have tried to resemble it into an E-commerce website which is in a running
form where users,sellers, and Administrators can work as they want in a real-life
Platform. We have made the Front end to enable the User Interface and User
Experience to the best of our abilities. Here our users can actually interact with our
website and do changes as they want to according to their scope in the project. It
ranges from selling and buying for users to make changes for Administrators and for
Sellers for selling their products. It also enables the site to work with all the necessary
constraints to put up an actual E-commerce site. We have connected the Database to
our actual website which maintains the recording accordingly, if we do any basic change
some change happens in or database.

## Tech-Stack Used
- `Frontend` - HTML, CSS, BootStrap 5, Jinja Template.
- `Backend` - Python, Flask, MySQL Database.
- We have populated our database with real and good amount of data to test to the website properly. Data coherency has been taken utmost care of.

We chose `Flask` as our backend becuase we needed the website to be working as quickly as possible to allign with our
project timeline. Also we chose `MySQL` as our database becuase we were working with it in our DBMS course in Undergrad.

## Steps to deploy the website ❓
- First clone this repository
- Then open the cloned folder
- We now need to restore the database from the dump.
- - Open the CMD in current folder and run the following command
```
mysql -u root -p online_store < Dump.sql
```
- Now create a virtual environment using the following command
```
py -m venv online_store
```
- Now activate this environment by running `.\online_store\Scripts\Activate.ps1`
- Now we need to pull up the project requirements. Run the below command
```
pip install -r .\requirements.txt
```
- This completes the setup process to run the website. Just run using running the `run.py` file 😀

# Demo of the website

## Login Screen
Firstly when we open the website we are shown the login screen.
- We are presented with three options
 - Use as Admin
 - Use as Seller
 - Use as a Customer
 
 ![image](https://user-images.githubusercontent.com/76804249/189930307-1b589e67-6929-42bd-8f95-26791a563861.png)

- Each role is then given a choice to Register or Login

![image](https://user-images.githubusercontent.com/76804249/189930533-d9417030-12ad-4fdb-b8cb-cbc4b78153d8.png)

- If the user chooses login then we show the authentication form

![image](https://user-images.githubusercontent.com/76804249/189930682-974ad142-c7c0-4bb3-b0b4-297e8048315e.png)

- If the entered password is incorrect then we show the error otherwise we login the user.

![image](https://user-images.githubusercontent.com/76804249/189930896-cb75eb5f-fa21-4806-ab96-5387abed6f79.png)

- If the user is not already register we ask the relevant details from him.

![image](https://user-images.githubusercontent.com/76804249/189931179-d0c77367-7732-4ec8-a270-895897884cb0.png)

## Shopping Screen
- Once the user is succesfully logged in we show him the product list

![image](https://user-images.githubusercontent.com/76804249/189931991-7129528d-059b-4705-b36d-c0d7760f40e5.png)

- He has the choice of adding the product to the cart. We give him confirmation once added a product succesfully.

![image](https://user-images.githubusercontent.com/76804249/189932723-824e8773-a96c-46f2-aebc-8fc5bb54e558.png)

- Then he can go to the cart and apply coupon code as well

![image](https://user-images.githubusercontent.com/76804249/189932935-66877493-52aa-4f86-91a0-8761e3af526a.png)

- We are then shown the price inclusive of discount and the payment and address is asked

![image](https://user-images.githubusercontent.com/76804249/189933944-768e09ba-e38e-4cc1-a4f9-de2378fbce53.png)

- We then show the user that order has been placed succesfully

![image](https://user-images.githubusercontent.com/76804249/189934185-e49aeae8-6b72-42b2-b92e-86e273146d43.png)

- If we login as seller than we can the products to the inventory

![image](https://user-images.githubusercontent.com/76804249/189934713-7e24517d-8ac5-4497-b457-131eb59b256b.png)

- If we login as Website Admin then we can do multiple things as shown

![image](https://user-images.githubusercontent.com/76804249/189935135-bddd315f-13c5-4816-947d-738a44108e5a.png)

- Say for example adding a new offer

![image](https://user-images.githubusercontent.com/76804249/189935575-259c4d78-50a2-4d58-9f5f-adb282dd0a03.png)


# Complete Description of the Project

## Scope of the Project
Our Project deals with the making and managing of an online retail store. In this project
our main objective is to make such a system which would help in the functioning of the
online retail system amongst the stakeholders involved in such a system. Our scope of
the project is mainly aiming to bridge the gap between people involved such as a
seller,customer , the person administering it and the delivery boys. We would have
different people to play different roles.
Here the Admin,Customer and the Seller all would be able to login to a page.
Specifically here we first take the Admin who would handle many requests and would
ensure the proper working amongst people other than the organization being involved in
the system. He would have all his details where he would have a name,ID,and a
password. He would be able to add sellers giving products in the market and adding
those products in the cart with their attributes. He would also be able to view the
product. The Admin can also add a delivery boy to add products and also has the
access to add offers for different orders as per their eligibility.
Then similarly a seller having their name, place of operation,password,email and phone
no would be able easily be able to sell the products.
The product sold would also have various attributes where the admin and customer
would be able to see it’s price,name, brand, measurement,unitand would also have an
ID.
Next we would have a customer who would have a name, password, email, mobile
number and also an ID who would have the liberty to give the feedback on the product
and is associated with the category and select the category. The customer now has the
power to give a rating to the delivery boy correspondimng to a order..
The Feedback would have a body to write the details as well as contain an ID to store it.
It would contain the date to be added and also the score to measure it.
We would have Categories containing the ID and the name to differentiate and the
products would also be added to a cart having the total cost and the value added with
it’s ID.
Finally the cart makes the orders so that it can finally go for purchasing where the order
would have it’s ID, the address it is being delivered to, the mode of payment and the
amount to be given. It would have the order date and also it’s time. The cart would also
have a final value as an attribute which is there after a offer is applied to it. Now offers
can be applied in the cart as well.The orders section would laos be assigned to a
particular delivery boy.
We would have a offers section as well which is mainly used to apply special discounts
to all the products that have been added in the product. The offer would contain a
promo code, an offer id,a maximum discount, minimum value and also a percentage
discount.
Next at last we have a deliver boy who carries out different orders throughout the
process. The delivery would have his password email id, phone number, as well as his
average rating. He would have an ID and also a name with first and last name. He
would be assigned to a order.
So all in all a person would be able sell his products to the customer where the process
would be managed by the admin and the order would be carried out by the delivery boy.
It would have all the added features to make the process more efficient and smooth.
We have also included Git for version control to ensure all members of the team have
the latest version of the database with them. We regularly update dumps of database on
Github.
Our final scope lies in identifying the products,users,admin ,orders ,sellers and delivery
boy and maintaining a proper cycle and interaction between all.

## Stake holders of the Project
There are multiple Stakeholders in this project mainly the project is centered around
customers and sellers along with it we also have admin and delivery boy as two more
of our stakeholders. Customers are important stakeholders who perform operations like
viewing products category wise, adding the products to cart, placing orders and giving
feedback on products. They can also add rating to the delivery boy corresponding to a
particular order.
Our other stakeholder seller sells various products which customers buy.
One other stakeholder here is the admin who maintains and adds data to our database
for online retail store like adding products, adding sellers along with that he can view the
orders customers have placed for processing them. The Admin also adds the delivery
boy while the delivery boy always gets assigned to a order when it is made.

## Assumptions in the Project
We have taken the following assumptions in our project.
1. First of all we have assumed that all orders will go through the cart and every
order will have a unique cart with unique cart ID and would be associated with
only one single customer. Also every customer will have one cart at a time to
place order.
2. Only a customer can add product feedback to a product by giving review and
rating to the products.
3. Each product will belong to some unique category and there are no categories
which don’t have any product.
4. Customer can view product directly also and can view it by selecting that
particular category also.
5. There can be multiple admins and each of them has the power to add
products,category and sellers.
6. Only admins can view details of all the orders placed by different customers while
a customer can view only his order
7. Each product can be sold by any of the multiple sellers and each seller can sell
multiple products
8. Seller can only know no of products of each type they have sold
9. We have also assumed each cart is associated with single order only and every
order is associated with single cart only
10. It is assumed in this project that all the products are sold at MRP and there is no
option of discount or coupon code or cashback. ASSUMPTION REMOVED.
11. We have made sure that offers are made according to a minimum price.It would
have a maximum discount and would have a percentage discount.
12. A cart can have a single offer only. But a single offer can be made to multiple
carts.
13.Only a single admin can add multiple offers.
14.Only a single admin can add multiple delivery boys.
15. A single delivery boy can be assigned to multiple orders
16. Multiple customers can give a particular rating value to multiple deliver boys
corresponding to multiple orders..
17.A customer can add a rating corresponding to its own order only
                                                