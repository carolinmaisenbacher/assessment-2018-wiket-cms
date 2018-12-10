# wiket-cms - Carolin Maisenbacher

## Installation

1. clone the repository to your local machine

2. virtualenv

virtualenv lets you create isolated development environments

How to install:
`$ pip install virtualenv`

More info at the official virtualenv website: https://virtualenv.pypa.io/en/latest/virtualenv/

3. postreSQL database

how to install:
`$ brew install postgresql`

create a database 'sechallenge' and add a user that has access to that table

`$ psql`

`$ CREATE DATABASE concierge; `



## Set-up
Change into the project folder and start the virtualenvironment:
`$ source bin/activate`

1. Install the requirements

`$ pip install -r requirements.txt`

2. adjust .env file

Go to the provided .env file and add
the DATABASE_USER and the DATABASE_SECRET
maybe you have to adjust the DATABASE_HOST as well.


3. create tables in database

`$ flask db upgrade`
this will now run all migrate files and create all necessary tables


4.fill database with sample data

`$ python sampledataloader.py`
this loads several csv files that I provided to fill the database with the data of 3 different restaurants.


5. run the application

`$ flask run`

The project will be available at 127.0.0.1:5000.


## How to use
1. go to the restaurant webiste

`127.0.0.1:5000/`
Here you now see a restaurant website that is filled with data that it get from an api provided by the flask backend.

2. Log into the Admin interface

`127.0.0.1:5000/admin`
you will be redirected to login at `127.0.0.1:5000/login`

you will need to first signup, so go to `127.0.0.1:5000/signup` and create a new user
now go back to the login and log in.


2. Change up the texts of the website.
`127.0.0.1:8000`

Put some products into the shopping cart.

Search products by category.

Visit your shopping cart. 

Delete some products from your shopping cart.

change the quantity of the products you have in the shopping cart.


## Walk through the code
There are three main parts of the application right now:
go to `app` and have a look at them 

1. main
in main.models all the database models for the restaurant are defined.
in main.routes the routes that are interesting for a user are defined, so `/` and `/login` `/admin` and so on.

2. authentification
this part is responsible to handle the state of the user, to log them in, to check whether their session is still valid.
in authentification.models the owner model is defined.
in authentification.routes are the apis provided with which you can login. 
all the routes have the prefix `/auth/` in case you want to visit them. I was not sure if a login is usually handled via an api, that is why I build two different kinds of logins and signups. One using the api -> `/login-api` and `/signup-api` (defined in main.routes) 
and one using normal forms (but the form validation is missing) -> `/login` and `/signup`
Both are working.

in authentification.sessions
I created the Sessions object that logs users in and out, checks if they are authenticated to do certain things and so on.

3. api
in the api section I just defined the apis to access different parts of the restaurant data. 
all the routes have the prefix `/api/` in case you want to visit them.

## How to stop
Press '^C' to quit the server.

To deactivate the virtualenv do this:
`$ deactivate`
