# E-Commerce
## Made with Django

[![N|Solid](https://twilio-cms-prod.s3.amazonaws.com/images/django-dark.width-808.png)](https://www.djangoproject.com/)

## Installation

This project requires [Python](https://www.python.org/download/releases/3.0/) v3.0+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd ecommerce
pip install -r requirements.txt
```

## Register Database Models

```sh
python manage.py migrate
python manage.py makemigrations core
## JUST TO BE SAFE, EXECUTE AGAIN  ##
python manage.py migrate
```
## Start Server

```sh
python manage.py runserver
Server wil be up and running at 127.0.0.1:8000
```

## Create superuser

```sh
python manage.py createsuperuser
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
```

## URLs

| URL | Description |
| ------ | ------ |
| / | Homepage |
| /admin | Admin Panel Login Page. |
| /accounts/login | Customers Login Page. |
| /accounts/signup | Customers Registration Page. |
| /product/<name> | Product Details Page |
| /order-summary | All Order Summary Total with Discounts |
| /checkout | Page for adding Billing and Shipping Information. Also You can add Discount Coupon  |
| /payment/<option> | Pay with Card/Saved Card with Stripe API |
| /request-refund | Request refund for particular order |
