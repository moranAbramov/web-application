from flask import request, flash, jsonify
from api import db, app
from api.models import People
from utils import apply_query, queries_to_json


# first page
@app.route('/')
def home_page():
    return "<h1>Welcome to the store!</h1>"


# Takes query as input and returns matching entries
@app.route('/store', methods=['GET'])
def get_query():
    # Check if a query was provided as part of the URL.
    # If no query is provided, display an error in the browser.
    args = request.args
    if "query" in args:
        queries = apply_query(args["query"])
        return queries_to_json(queries)
    else:
        flash("No query was requested", 'error')
        return "GET request done!"


# Take entity and stores it
@app.route('/store', methods=['POST'])
def new_entity():
    # Create sql tables for our data models
    db.create_all()
    if not request.json['id'] or not request.json['title'] or not request.json['content'] or not request.json['views']\
            or not request.json['timestamp']:
        flash('Please enter all the fields', 'error')  # missing fields
    else:
        new_people = People(id=request.json['id'],
                            title=request.json['title'],
                            content=request.json['content'],
                            views=request.json['views'],
                            timestamp=request.json['timestamp'])   # Create an instance of the People class
        db.session.add(new_people)   # Adds a new record to the database
        db.session.commit()  # Commits all changes
        flash('Record was successfully added')
    return "POST request done!"



