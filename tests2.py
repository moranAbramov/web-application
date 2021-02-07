import flask_unittest
from flask import Flask
from config import Config
from api import db


PEOPLE = {"id": "first-post",
                  "title": "My First Post",
                  "content": "Hello World!",
                  "views": 1,
                  "timestamp": 1555832341}


class TestFoo(flask_unittest.AppClientTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config.from_object(Config)
        app.config['TESTING'] = True
        db.drop_all()
        db.create_all()
        return app

    def setUp(self, app, client):
        # Perform set up before each test, using api and client
        pass

    def tearDown(self, app, client):
        # Perform tear down after each test, using api and client
        pass

    '''
    Note: the setUp and tearDown method don't need to be explicitly declared
    if they don't do anything (like in here) - this is just an example
    Only declare the setUp and tearDown methods with a body, same as regular unittest testcases
    '''

    def test_foo_with_both(self, app, client):
        # Use the api and client here
        # Example of registering a user and checking if the entry exists in db (on a hypothetical api)
        ans = client.get('/')
        # test that the user was inserted into the database
        with app.app_context():
            self.assertIsNotNone(db.select())

    # def test_bar_with_both(self, api, client):
    #     # Use the api and client here
    #     # Example of creating a post and checking if the entry exists in db (on a hypothetical api)
    #     client.post('/create', data={'title': 'created', 'body': ''})
    #
    #     with api.app_context():
    #         db = get_db()
    #         count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
    #         self.assertEqual(count, 2)


if __name__ == "__main__":
    flask_unittest.run()
