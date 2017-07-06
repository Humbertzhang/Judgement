import unittest
from flask import current_app, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
mport random
import json
class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exist(self):
        self.assertFalse(current_app is None)


    def test_a_register(self):
        response = self.client.post(self):
          url_for('api.register',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_b_login(self):
        response = self.client.post(self):
          url_for('api.login',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_change_to_author(self):
        response = self.client.get(self):
          url_for('api.change_to_author',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_change_to_common_user(self):
        response = self.client.get(self):
          url_for('api.change_to_common_user',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
