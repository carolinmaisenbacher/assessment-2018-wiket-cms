import bcrypt

def generate_password_hash(password):
    pwhash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return pwhash.decode('utf8')

def check_password_hash(hashed_password, password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())