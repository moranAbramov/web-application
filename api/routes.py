from flask import request, flash
from api import db, app
from api.models import People


# first page
@app.route('/')
def home_page():
    new_people = People(id="ffffff",
                        title="ffffff",
                        content="ffffff",
                        views=11511,
                        timestamp=11511)  # Create an instance of the People class
    db.session.add(new_people)  # Adds new People record to database
    db.session.commit()  # Commits all changes
    return "<h1>frgg</h1><p>SPARE</p>"


@app.route('/store', methods=['GET'])
def get_query():
    # Check if a query was provided as part of the URL.
    # If no query is provided, display an error in the browser.
    args = request.args
    if "query" in args:
        ans = People.query.all()
        return ans
    return "No query string received"


@app.route('/store', methods=['POST'])
def new_entity():
    # Create sql tables for our data models
    db.create_all()
    if not request.json['id'] or not request.json['title'] or not request.json['content'] or not request.json['views']\
            or not request.json['timestamp']:
        flash('Please enter all the fields', 'error')  # missing information
    else:
        new_people = People(id=request.json['id'],
                            title=request.json['title'],
                            content=request.json['content'],
                            views=request.json['views'],
                            timestamp=request.json['timestamp'])   # Create an instance of the People class
        db.session.add(new_people)   # Adds new People record to database
        db.session.commit()  # Commits all changes
        flash('Record was successfully added')
#    return "People adds successfully"



