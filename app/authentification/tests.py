import unittest
from app import create_app
from app.config import TestConfig
from app.authentification.routes import login
import requests
import time
import json
from app.authentification import routes
from unittest.mock import MagicMock



class SignUpCase(unittest.TestCase):
 
    def setUp(self):
       self.hostname = "http://127.0.0.1:5000/"
       self.app = create_app(TestConfig)
       self.headers = {'content-type': 'application/json'}

    def tearDown(self):
        routes.users = []


    # when a new user successfully signs up with a email, and a password the userid should be returned and the status code should be 201
    def test_valid_sign_up(self):     
        data = json.dumps({'email' : 'example2@mail.com', 'password': 'paspythosword'})
        
        with self.app.test_client() as c:
            result = c.post(self.hostname + 'auth/signup', headers=self.headers, data=data)
        
        self.assertEqual(result.status_code, 201, "User was not created after a json object with email and password was posted")
        self.assertEqual([*result.json], ["userId"], "Successful sign up does not return the userId")
        

    
    # if a user wants to sign up with a username that is already taken, a 400 should be returned saying, that username is already taken
    def test_signup_with_already_used_email(self):
        data = json.dumps({'email' : 'example2@mail.com', 'password': 'paspythosword'})
        
        with self.app.test_client() as c:
            result1 = c.post(self.hostname + 'auth/signup', headers=self.headers, data=data)
            result2 = c.post(self.hostname + 'auth/signup', headers=self.headers, data=data)
        
        self.assertEqual(result2.status_code, 401, "User was able to signup with an email that was used before")
        self.assertEqual([*result2.json], ["error"], "No error was raised when user tried to signup with a email that was used before")

    # a user needs to provide a password
    def test_signup_without_password(self):
        data = json.dumps({'email' : 'example2@mail.com', 'password': ''})
        
        with self.app.test_client() as c:
            result = c.post(self.hostname + 'auth/signup', headers=self.headers, data=data)
        
        self.assertEqual(result.status_code, 401, "User could sign up without providing a password")
        self.assertEqual([*result.json], ["error"], "On sign up, not providing a password did not raise an error")

    # a user needs to provide a email
    def test_signup_without_email(self):
        data = json.dumps({'email' : '', 'password': '123'})
        
        with self.app.test_client() as c:
            result = c.post(self.hostname + 'auth/signup', headers=self.headers, data=data)
        
        self.assertEqual(result.status_code, 401, "User could sign up without providing an email")
        self.assertEqual([*result.json], ["error"], "On sign up, not providing an email did not raise an error")

    ###
    # as user needs to provide a VALID email
    ###

    ## http get request is not allowed on /auth/signup
    def test_signup_with_get_request(self):
        data = json.dumps({'email' : 'example@mail.com', 'password': '123'})
        
        with self.app.test_client() as c:
            result = c.get(self.hostname + 'auth/signup', headers=self.headers, data=data)

        self.assertEqual(result.status_code, 405, "Get request on /auth/signup should not be allowed")

    

    # after signup a user should be saved, with a userid
    ## the users password need to be saved as a hash


    # a user that signed up once should be able to log into the application when he returns to the side at some point later in time
    

    # the login function needs to be tested
    def test_finish(self):
        self.assertFalse(True, "finish the tests")




if __name__ == '__main__':
    unittest.main()     