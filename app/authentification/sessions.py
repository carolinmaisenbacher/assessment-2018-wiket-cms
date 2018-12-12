from os import urandom
from flask import make_response, jsonify


def login(user, response):
    sessionId = sessions.create(user)
    response.set_cookie("sessionId", value = str(sessionId))
    return response

def logout(sessionId):
    try:
        sessions.remove(int(sessionId))
    except ValueError as e:
        return False
    return True
    
    
def is_logged_in(request):
    try:
        sessionId = int(request.cookies.get("sessionId"))
    except ValueError as e:
        return False
    except TypeError as a:
        return False

    if sessionId:
        return Sessions.is_valid(sessionId)
    else:
        return False 

def is_authorized(request, restaurant_id):
    if not is_logged_in(request):
        return False
    info = get_user_information(request)
    if info["restaurant_id"] == restaurant_id:
        return info
    return False

def get_user_information(request):
    sessionId = int(request.cookies.get("sessionId"))
    return sessions.sessions[sessionId]

# should be implemented as a singleton
# is not allowed to be be created somewhere else in the program
class Sessions():
    sessions = {}

    # I know it is totally not secure to mess with the random number generator, but I just didn't manage to store the byte string correctly in the cookie
    # next time I would use a solution that is out there already
    @classmethod
    def create(cls, user):
        random = urandom(20)
        sessionId = ''
        for byte in random:
            sessionId += str(byte)
        sessionId = int(sessionId)
        cls.sessions[sessionId] = {
            "user_id" : user.id,
            "restaurant_id" : user.restaurant_id
        }
        return sessionId

    @classmethod
    def is_valid(cls, sessionId):
        if sessionId in cls.sessions:
            return True
        return False

    @classmethod
    def remove(cls, sessionId):
        if sessionId in cls.sessions:
            cls.sessions.pop(sessionId)
    
    

    



sessions = Sessions()