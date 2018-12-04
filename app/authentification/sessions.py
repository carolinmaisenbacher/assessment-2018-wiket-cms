from os import urandom

def login():
    pass

def logout():
    pass

class Sessions():
    def __init__(self):
        self.sessions = {}

    def create(self, userId):
        sessionId = urandom(20)
        self.sessions[sessionId] = userId
        return sessionId

    def check(self, sessionId):
        return self.sessions.get(sessionId)

