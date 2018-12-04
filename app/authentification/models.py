from app import db
from hash import generate_password_hash

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=False)
    last_name = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password= db.Column(db.String(128))

    def __repr__(self):
        return '<Owner {}>'.format(self.email) 

    @classmethod
    def create_owner(cls, first_name, last_name, email, password):
        try:
            cls.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = generate_password_hash(password)
            )
        except IntegrityError:
            raise ValueError("owner already exists")