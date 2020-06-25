import requests
from flask import Flask, request, render_template, jsonify, make_response
import json
import urllib.parse as urlparse
from urllib.parse import unquote
import sqlite3
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__, template_folder='templates')
# app.config["MONGO_URI"] = "mongodb://localhost:27017/subspacedb"
# mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/naiveDecider', methods = ['GET', 'POST'])
def naiveDecider():
    return render_template('naiveDecider.html')

@app.route('/addOption', methods = ['GET', 'POST'])
def addOption():
    option = request.form['option']
    return render_template('naiveDecider.html')

# @app.route('/signup')
# def signup():
#     return render_template('signup.html')

# @app.route('/create_account', methods = ['GET', 'POST'])
# def create_account():
#     name = request.form['name']
#     dob = request.form['dob']
#     uni = request.form['uni']
#     DLN = request.form['DLN']
#     address = request.form['address']
#     email = request.form['email']
#     password = request.form['password']
#     error = ""

#     # lets encrypt the password for security.
#     b_password = str.encode(password)
#     salt = bcrypt.gensalt(rounds=10)
#     hashed = bcrypt.hashpw(b_password, salt)  
#     # hashed = hashed.decode('utf-8')

#     try:
#         mongo.db.users.insert(
#             {"email": email, "password": hashed, "name": name, "dob": dob, "uni": uni, "DLN": DLN, "address": address}
#             )
#     except:
#         error = "Email already exists"
#     return render_template('signup-thankyou.html', name = name, error = error)

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/load_user_home', methods = ['GET', 'POST'])
# def load_user_home():
#     email = request.form['email']
#     password = request.form['password']



#     user = mongo.db.users.find({"email": email})

#     if not user: 
#         error = "No user user with this email/password was found. Please try again."
#         return render_template('login.html', error = error)
    
#     # check password
#     b_password = str.encode(password)
#     hashed = user[0]['password']
#     valid = bcrypt.checkpw(b_password, hashed)
#     if not valid:
#         error = "No user user with this email/password was found. Please try again."
#         return render_template('login.html', error = error)
    
#     # set cookie
    
#     return render_template('user_home.html', name = user[0]['name'])

# @app.route('/view_listings', methods = ['GET', 'POST'])
# def view_listings():
#     return render_template('view_listings.html')

# @app.route('/create_listing', methods = ['GET', 'POST'])
# def create_listing():
#     return render_template('create_listing.html')

# @app.route('/find_space')
# def find_space():
#     return render_template('find_space.html')

if __name__== "__main__":
    app.run()