// after installing mongoDB, run mongod in the background
// open mongo shell using mongo and enter these commands line by line
// then run app.py using python app.py 
// make sure to pip install flask and pymongo
use subspacedb
db.createCollection("users")
db.users.createIndex( { "email": 1 }, { unique: true } )
db.createCollection("listings")

