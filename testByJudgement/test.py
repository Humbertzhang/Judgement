import unittest
from flask import current_app, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import random
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

    #Test forgive
    def test_c_forgive(self):
        response = self.client.post(self):
          url_for('api.forgive',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    #Test login
    def test_b_login(self):
        response = self.client.post(self):
          url_for('api.login',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    #Test get_info
    def test_c_get_info(self):
        response = self.client.get(self):
          url_for('api.get_info',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    #Test signup
    def test_a_signup(self):
        response = self.client.post(self):
          url_for('api.signup',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    #Test upload_time
    def test_c_upload_time(self):
        response = self.client.XXXX(self):
          url_for('api.upload_time',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
