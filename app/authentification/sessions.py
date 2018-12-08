from os import urandom
from flask import make_response, jsonify


def login(user, response):
    sessionId = sessions.create(user.id)
    response.set_cookie("sessionId", value = str(sessionId))
    return response

def logout(sessionId):
    sessions.remove(int(sessionId))

def is_logged_in(request):
    try:
        sessionId = request.cookies.get("sessionId")
    except ValueError as e:
        return False
    if sessionId:
        return is_valid_sessionId(sessionId)
    else:
        return False 

def is_valid_sessionId(sessionId):
    try:
        if sessions.check(int(sessionId)):
            return True
    except ValueError as e:
        return False
    return False

# should be implemented as a singleton
class Sessions():
    def __init__(self):
        self.sessions = {}

    # I know it is totally not secure to mess with the random number generator, but I just didn't manage to store the byte string correctly in the cookie
    # next time I would use a solution that is out there already
    def create(self, userId):
        random = urandom(20)
        sessionId = ''
        for byte in random:
            sessionId += str(byte)
        sessionId = int(sessionId)
        self.sessions[sessionId] = userId
        return sessionId


    def check(self, sessionId):
        if sessionId in self.sessions:
            return True
        return False

    def remove(self, sessionId):
        if sessionId in self.sessions:
            self.sessions.pop(sessionId)
    
    def get_user_id(self, sessionId):
        return self.sessions[int(sessionId)].value



sessions = Sessions()