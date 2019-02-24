## Flask - Microframework which helps us to build web applications

### DOCKORIZED RESTFUL API IN PYTHON

#Import flask
from flask import Flask
import markdown
import os
import shelve
# Create Flask instance
from flask import g
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open('customers.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
	##Open the readme file and display it as HTML content
	with open(os.path.dirname(app.root_path) + '/Readme.md', 'r') as file:
		#Read the content of the file
		content = file.read()

		#Convert the file to html using markdown
		return markdown.markdown(content)


#Using flask Restful API to create easy 
## Create a class for each endpoint and create the method which we want acess - get, post

class CustomerList(Resource):
	#Get method
	def get(self):
		shelf = get_db()
		keys = list(shelf.keys())
		customer = []
		for key in keys:
			customer.append(shelf[key])
		return {'message': 'Success', 'data': customer}, 200

	def post(self):
		#Request parser provides uniform access to any variable
		parser = reqparse.RequestParser()

		parser.add_argument('identifier', required=True, type=str)
		parser.add_argument('name', required = True, type=str)
		parser.add_argument('subscription', required = True, type=str)
		parser.add_argument('size', required = True, type=str)

		#Parse the arguments into the object
		args = parser.parse_args()

		shelf = get_db()
		shelf[args['identifier']] = args #store whole object that we receive

		return {'message': 'Customer registered', 'data': args}, 201

class Customer(Resource): #class to represent individual resource
	def get(self, identifier): #getting the identifier parameter as a part of the get function
		shelf = get_db()

		#if any key does not appear in shelf, return 404 not found error
		if not (identifier in shelf):
			return {'message': 'Customer Not found', 'data': {}}, 404

		return {'message': 'Customer found', 'data': shelf[identifier]}, 200

	def delete(self, identifier):
		shelf = get_db()

		#if any key does not appear in shelf, return 404 not found error
		if not (identifier in shelf):
			return {'message': 'Customer Not found', 'data': {}}, 404

		del shelf[identifier]
		return '', 204


api.add_resource(CustomerList, '/customer')
api.add_resource(Customer, '/customer/<string:identifier>')