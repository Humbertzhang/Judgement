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


    #--------API FILE NAME:test_apis/forgive.py------------------------------------------

    #Test forgive
    def test_c_forgive(self):
        response = self.client.post(
            url_for('api.forgive',_external=True),
            data = json.dumps({
                "my_id":'test',
            }),
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)


    #--------API FILE NAME:test_apis/signin.py------------------------------------------

    #Test login
    def test_b_login(self):
        response = self.client.post(
            url_for('api.login',_external=True),
            data = json.dumps({
                "username":'test',
                "password":'test',
            }),
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)


    #--------API FILE NAME:test_apis/__init__.py------------------------------------------


    #--------API FILE NAME:test_apis/getinfo.py------------------------------------------

    #Test get_info
    def test_c_get_info(self):
        response = self.client.get(
            url_for('api.get_info',_external=True),
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)


    #--------API FILE NAME:test_apis/signup.py------------------------------------------

    #Test signup
    def test_a_signup(self):
        response = self.client.post(
            url_for('api.signup',_external=True),
            data = json.dumps({
                "username":'test',
                "password":'test',
                "email":'test',
            }),
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)


    #--------API FILE NAME:test_apis/uploadtime.py------------------------------------------

    #Test upload_time
    def test_c_upload_time(self):
        response = self.client.put(
            url_for('api.upload_time',_external=True),
            data = json.dumps({
                "my_id":'test',
                "time":'test',
            }),
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

