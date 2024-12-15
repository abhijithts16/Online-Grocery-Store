# An E-Commerce Grocery Store website using Flask
The E-Commerce Grocery Store Web Application is a dynamic online platform designed for managing an e-commerce store. It offers core functionalities such as product management, order processing, and secure user interactions. The application is built using Flask, MySQL, and various security best practices to ensure data privacy, integrity, and safe transactions. The main focus of this project is to deliver a user-friendly, secure online shopping experience by implementing strong security measures, such as authentication, authorization, and secure session management.

## Technology Stack
- **Frontend**: HTML, CSS, Bootstrap 5, Jinja Templates
- **Backend**: Python (Flask)
- **Database**: MySQL
- **Security Libraries**: Flask-Bcrypt, Flask-WTF
- **Testing Tools**: Bandit (Static Application Security Testing), Browser Developer Tools (for security verification)

## Features and Security Objectives

### Major Features
### 1. User Management
- **User Registration**: Allows new users to sign up for the platform.
- **Login and Authentication**: Enables users to log in securely.
- **User Roles**: Supports distinct roles such as Admin, Seller, and Customer.
### 2. Admin Functionalities
- **View Orders**: Review and manage customer orders.
- **Add Delivery Personnel**: Register new delivery boys to the system.
- **Add New Offers**: Create and manage promotional codes.
- **Add New Products**: Upload and manage product listings.
- **Add New Sellers**: Onboard and manage sellers on the platform.
### 3. Seller Functionalities
- **Manage Product Inventory**: Add or update the quantity of existing products.
### 4. Customer Functionalities
- **Browse Products**: View available products with details.
- **Cart Management**:
  - Add items to the cart.
  - Remove items from the cart.
- **Order Placement**: Place orders for items added to the cart.

### Security Objectives
- **Authentication**: Secure user authentication with hashed passwords.
- **Authorization**: Role-based access control to ensure users have appropriate permissions.
- **Session Management**: Secure session handling with appropriate cookie attributes to prevent session hijacking.
- **Data Validation and Sanitization**: Prevent SQL injection and XSS attacks by validating and sanitizing user input.
- **Error Handling**: Graceful error handling with informative error messages.
- **Auditing and Logging**:Track user actions and log important events for monitoring and debugging.
- **Proper Security Configurations**:To protect against Clickjacking, CSRF and MIME Type Sniffing.

## Project Structure
**market/**: Contains the main application code.
- **init.py**: Initializes the Flask application.
- **routes.py**: Defines the routes and views for the application.
- **models.py**: Defines the database models.
- **forms.py**: Defines the forms used in the application.

**static/**: Contains static files like CSS and uploads.

**templates/**: Contains HTML templates for rendering views.

**run.py**: Entry point to run the Flask application.

**requirements.txt**: Lists the dependencies required for the project.

**README.md**: Project documentation.

## Setup and Installation Instructions -
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

## Usage Guidelines
Firstly when we open the website we are shown the login screen.
We are presented with three options
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

## Security Improvements

The application implements the following key security improvements:

1. **Authentication**: 
   - Passwords are hashed using **Flask-Bcrypt** for secure storage.

2. **Authorization**:
   - Role-based access control (RBAC) is used to ensure that users only have access to the appropriate resources.

3. **Input Validation and Sanitization**:
   - User input is validated and sanitized using **WTForms** and **markupsafe.escape**  to prevent attacks like SQL injection and XSS.

4. **Session Management**:
   - Session cookies are secured with **HttpOnly** and **Secure** flags to prevent unauthorized access.

5. **Content Security**:
   - A strong **Content Security Policy (CSP)** and other headers like **X-Frame-Options** and **X-XSS-Protection** are implemented to prevent clickjacking and XSS attacks.

6. **CSRF Protection**:
   - CSRF tokens are included in forms to protect against cross-site request forgery attacks.

7. **Error Handling**:
   - Custom error handlers were implemented to handle common HTTP errors gracefully.

8. **Auditing and Logging**:
   - User actions and application events are logged for monitoring and debugging purposes.

9. **SQLAlchemy Database Interactions**:
   - SQLAlchemy ORM is used to reduce the risk of SQL injection and simplify database interactions.

## Testing Process

### Functional Testing
Functional testing was performed to ensure key security features are functioning correctly. Below is a summary of the key test cases executed:

| Test Case                                 | Steps Performed                                             | Expected Result                                         | Actual Result                                           |
|-------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| **Verify Unauthorized Access (Authentication)** | Attempt to access admin page without logging in.            | Should redirect to login page or show error.            | Unauthorized access blocked as expected.                |
| **Verify Role-Based Access Control (Authorization)** | Attempt to access admin page as a regular user.             | Regular users should be denied access.                  | Access denied as expected.                              |
| **Verify Input Validation and Sanitization** | Submit malicious payload (`' OR 1=1; --`) in registration form. | Input should be sanitized.                              | Input sanitized properly, no SQL injection.             |
| **Verify Secure Session Handling**        | Inspect cookies using developer tools.                      | Cookies should have HttpOnly and Secure flags.           | HttpOnly and Secure flags correctly set.                |

### Static Application Security Testing (SAST)
Static Application Security Testing (SAST) was performed using **Bandit**, which scans Python code for common security vulnerabilities. The scan identified the following issues:
- **Hardcoded Secret**: A medium-level risk from a hardcoded password (`app.secret_key`).
- **Unsafe YAML loading**: High-confidence issue due to `yaml.load`, which could instantiate arbitrary objects.
- **Insecure Randomness**: Use of `random.choice` and `random.randint` for cryptographic purposes.

These issues have been addressed or noted for future improvement to ensure the application follows secure coding standards.

## Contributions and References

This project is built as part of a learning exercise and security enhancement. You can refer to the original repository here: [E-Commerce Grocery Store](https://github.com/vibhorag101/ECommerce-Grocery-Store).
                                                