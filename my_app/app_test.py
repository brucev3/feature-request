import os
from my_app import app, db
import unittest2 as unittest
import tempfile

class FeaturesTestCase(unittest.TestCase):

    def setUp(self):
        self.test_db_file = tempfile.mkstemp()[1]
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + self.test_db_file
        app.config['TESTING'] = True

        app.config['WTF_CSRF_ENABLED'] = False

        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        os.remove(self.test_db_file)

    def test_home(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)

    def test_features(self):
        "Test Featureslist page"
        rv = self.app.get('/features')
        self.assertEqual(rv.status_code, 301)

    def test_features_(self):
        "Test Featureslist page one"
        rv = self.app.get('/features/1')
        self.assertEqual(rv.status_code, 200)

    def test_feature(self):
        "Test Feature page"
        rv = self.app.get('/feature/1')
        self.assertEqual(rv.status_code, 200)

if __name__ == '__main__':
    unittest.main()