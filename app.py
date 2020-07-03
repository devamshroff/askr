import requests
from flask import Flask, request, render_template, jsonify, make_response
import json
from werkzeug.security import generate_password_hash, check_password_hash

# import urllib.parse as urlparse
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
try:
	from urllib.parse import unquote
except ImportError:
	from urlparse import unquote

import sqlite3
from flask_pymongo import PyMongo
import bcrypt
from random import randint

app = Flask(__name__, template_folder='templates')
app.config["MONGO_URI"] = "mongodb://localhost:27017/subspacedb"
mongo = PyMongo(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/naiveDecider', methods = ['GET', 'POST'])
def naiveDecider():
    if len(request.form) == 0:
        print("request.form is null")
        return render_template('naiveDecider.html')
    # return render_template('naiveDecider.html')
    options = request.form['options']
    optionList = options.split(',')
    n = randint(0, len(optionList)-1)
    print(optionList[n])
    return render_template('naiveDecider.html', options = options, ans = optionList[n])

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	return render_template('signup.html')

@app.route('/create_account', methods = ['GET', 'POST'])
def create_account():

	email = request.form['email']
	password = request.form['password']
	error = ""

#	lets encrypt the password for security.
	password = generate_password_hash(password, method='sha256')

	if (len(email) == 0 or len(password) == 0):
		error = "Missing email or password"
		return render_template('signup.html', error = error)
	try:
		mongo.db.users.insert({"email": email, "password": password})
	except:
		error = "Email already exists, try again"
		return render_template('signup.html', error =  error)
	return render_template('naiveDecider.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	return render_template('login.html')

@app.route('/load_user_home', methods = ['GET', 'POST'])
def load_user_home():
	email = request.form['email']
	password = request.form['password']

	user = mongo.db.users.find({"email": email})
	email_exists = mongo.db.users.find( { "email": { "$in":[email] } } ).count()

	if email_exists == 0:
		error = "No user user with this email was found. Please try again."
		return render_template('login.html', error = error)
    
#	check password
	if not user or not check_password_hash(user[0]['password'], password):
		error = "Please check login details and try again."
		return render_template('login.html', error = error)
    
#     # set cookie
    
	return render_template('naiveDecider.html')

if __name__== "__main__":
    app.run()
