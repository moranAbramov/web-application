import unittest
from api import app, db

PEOPLE = {"id": "first-post",
                  "title": "My First Post",
                  "content": "Hello World!",
                  "views": 1,
                  "timestamp": 1555832341}


class TestStore(unittest.TestCase):

    def setUp(self):
        # Perform set up before each test, using api and client
        # api = Flask(__name__)
        # api.config.from_object(Config)
        app.testing = True
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        pass

    def tearDown(self):
        # Perform tear down after each test, using api and client
        db.session.remove()
        db.drop_all()
        pass

    def test_main(self):
        with self.app as client:
            client.environ_base['REMOTE_PORT'] = 5000
            # send data as POST form to endpoint
            sent = PEOPLE
            result = client.post('/store', sent)
            self.assertEqual(result.status_code, 200)


    # def test_store_post(self):
        # Use the api and client here
        # Example of registering a user and checking if the entry exists in db (on a hypothetical api)
        # result = self.api.post('/store', data=PEOPLE)

        # db_entities = People.query.all()

        # # test that the user was inserted into the database
        # with self.api.app_context():
        #     self.assertIsNotNone(db.execute("select * from user where id = PEOPLE['id']").fetchone())

        # assert the status code of the response
        # self.assertEqual(result.status_code, 200)

    # def test_bar_with_both(self, api, client):
    #     # Use the api and client here
    #     # Example of creating a post and checking if the entry exists in db (on a hypothetical api)
    #     client.post('/create', data={'title': 'created', 'body': ''})

        # with api.app_context():
        #     db = get_db()
        #     count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        #     self.assertEqual(count, 2)


# class MyTest(unittest.TestCase):
#
#     def test_post_request():
#         dict_to_send = {"id": "first-post",
#                       "title": "My First Post",
#                       "content": "Hello World!",
#                       "views": 1,
#                       "timestamp": 1555832341
#                      }
#         res = request.post('http://localhost:5000/store', json=dict_to_send)
#         print('response from server:',res.text)
#         return res.json()
if __name__ == "__main__":
    unittest.main()