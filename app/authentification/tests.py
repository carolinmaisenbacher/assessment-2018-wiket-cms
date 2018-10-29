import unittest
import time
import json
import requests

from app import create_app
from app.config import TestConfig

from app.authentification import routes


class SignUpCase(unittest.TestCase):
 
    def setUp(self):
       self.hostname = "http://127.0.0.1:5000/"
       self.app = create_app(TestConfig)
       self.headers = {'content-type': 'application/json'}
       routes.users = []

    def tearDown(self):
        pass


    # when a new user successfully signs up with a email, and a password the userid should be returned and the status code should be 201
    def test_valid_sign_up_creates_user(self):     
        email = 'example2@mail.com'
        password = 'password'
        data = {'email' : email, 'password': password}
        
        result = self.post_to_signup(data)
        user = routes.User.find(email)

        self.assertEqual(result.status_code, 201, "User was not created after a json object with email and password was posted")
        self.assertEqual(result.json, {"userId" : user.id}, "Successful sign up does not return the correct userId")
        self.assertIn("Set-Cookie", result.headers)
        self.assertTrue(user, "User was not saved after signup")
        self.assertEqual(user.email, email)
        self.assertNotEqual(user.hashed_password, password, "Password of user is not hashed.")
        # ???? Would I test, if the password is correctly hashed? I feel like that would be more than just testing the functionality.
        self.assertTrue(user.id)


    def test_signup_with_incomplete_json(self):
        data_just_email = {'email': 'password'}
        data_just_password = {'password': 'password'}
        data_empty = {}
        
        result_just_email = self.post_to_signup(data_just_email)
        result_just_password = self.post_to_signup(data_just_password)
        result_empty_json = self.post_to_signup(data_empty)
        
        self.assertEqual(result_just_email.status_code, 400)
        self.assertEqual(result_just_password.status_code, 400)
        self.assertEqual(result_empty_json.status_code, 400)


    # if a user wants to sign up with a username that is already taken, a 400 should be returned saying, that username is already taken
    def test_signup_with_already_used_email(self):
        data = {'email' : 'example2@mail.com', 'password': 'password'}
        
        result1 = self.post_to_signup(data)
        result2 = self.post_to_signup(data)
        
        self.assertEqual(result2.status_code, 401, "User was able to signup with an email that was used before")
        self.assertEqual([*result2.json], ["error"], "No error was raised when user tried to signup with a email that was used before")


    # a user needs to provide a password
    def test_signup_without_password(self):
        data = {'email' : 'example2@mail.com', 'password': ''}
        
        result = self.post_to_signup(data)
        
        self.assertEqual(result.status_code, 401, "User could sign up without providing a password")
        self.assertEqual([*result.json], ["error"], "On sign up, not providing a password did not raise an error")


    # a user needs to provide a email
    def test_signup_without_email(self):
        data = {'email' : '', 'password': 'password'}
        
        result = self.post_to_signup(data)
        
        self.assertEqual(result.status_code, 401, "User could sign up without providing an email")
        self.assertEqual([*result.json], ["error"], "On sign up, not providing an email did not raise an error")


    ###
    ###### as user needs to provide a VALID email
    ###

    ## http get request is not allowed on /auth/signup
    def test_signup_with_get_request(self):
        data = json.dumps({'email' : 'example@mail.com', 'password': '123'})
        
        with self.app.test_client() as c:
            result = c.get(self.hostname + 'auth/signup', headers=self.headers, data=data)

        self.assertEqual(result.status_code, 405, "Get request to /auth/signup should not be allowed")


    # after signup a user should be saved, with a userid
    

    ###
    # a user that signed up once should be able to log into the application when he returns to the side at some point later in time
    ###
    def post_to_signup(self, content):
        json_content = json.dumps(content)
        headers = {'content-type': 'application/json'}
        with self.app.test_client() as c:
            return c.post(self.hostname + 'auth/signup', headers=headers, data=json_content)


    

class LogInCase(unittest.TestCase):

    def setUp(self):
        self.hostname = "http://127.0.0.1:5000/"
        self.app = create_app(TestConfig)
        self.headers = {'content-type': 'application/json'}
        routes.users = []

        self.email = 'example2@mail.com'
        self.password = 'password'
        self.data = {'email' : self.email, 'password': self.password}
        with self.app.test_client() as c:
            return c.post(self.hostname + 'auth/signup', headers=self.headers, data=json.dumps(self.data))


    def tearDown(self):
        pass


    def test_valid_login(self):
        
        result = self.post_to_login(self.data)
        user = routes.User.find(self.email)

        self.assertEqual(result.status_code, 200, "Existing user was not able to log in.")
        self.assertEqual(result.json, {"userId" : user.id}, "Successful log up does not return the correct userId")
        self.assertIn("Set-Cookie", result.headers)


    def test_login_with_incomplete_json(self):
        data_just_email = {'email': self.email}
        data_just_password = {'password': self.password}
        data_empty = {}
        
        result_just_email = self.post_to_login(data_just_email)
        result_just_password = self.post_to_login(data_just_password)
        result_empty_json = self.post_to_login(data_empty)
        
        self.assertEqual(result_just_email.status_code, 400)
        self.assertEqual(result_just_password.status_code, 400)
        self.assertEqual(result_empty_json.status_code, 400)


    def test_login_with_wrong_email(self):
        data = {'email' : 'example2@code.berlin', 'password': 'password'}
        
        result = self.post_to_login(data)

        self.assertEqual(result.status_code, 401, "User was able to signup with a wrong email")
        self.assertEqual([*result.json], ["error"], "No error was raised when user tried to signup with a wrong email")


    def test_login_with_wrong_password(self):
        data = {'email' : self.email, 'password': 'wrong'}
        
        result = self.post_to_login(data)

        self.assertEqual(result.status_code, 401, "User was able to signup with a wrong password")
        self.assertEqual([*result.json], ["error"], "No error was raised when user tried to signup with the wrong password")


    # a user needs to provide a password
    def test_login_without_password(self):
        data = {'email' : self.email, 'password': ''}
        
        result = self.post_to_login(data)
        
        self.assertEqual(result.status_code, 401, "User could sign up without providing a password")
        self.assertEqual([*result.json], ["error"], "On sign up, not providing a password did not raise an error")


    # a user needs to provide a email
    def test_login_without_email(self):
        data = {'email' : '', 'password': self.password}
        
        result = self.post_to_login(data)
        
        self.assertEqual(result.status_code, 401, "User could sign up without providing an email")
        self.assertEqual([*result.json], ["error"], "On sign up, not providing an email did not raise an error")


    def post_to_login(self, content):
        json_content = json.dumps(content)
        headers = {'content-type': 'application/json'}
        with self.app.test_client() as c:
            return c.post(self.hostname + 'auth/login', headers=headers, data=json_content)


if __name__ == '__main__':
    unittest.main()     