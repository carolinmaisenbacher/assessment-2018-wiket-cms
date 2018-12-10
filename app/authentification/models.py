from app import db
from app.authentification.hash import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=False)
    last_name = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password= db.Column(db.String(60))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)


    def __repr__(self):
        return '<Owner {}>'.format(self.email) 

    @classmethod
    def create_owner(cls, first_name, last_name, email, password):
        try:
            owner = Owner(first_name = first_name,
                last_name = last_name,
                email = email,
                # prevents double encoding by the database
                password =generate_password_hash(password),
                
                # still needs to be done.
                
                restaurant_id= 1
            )
            db.session.add(owner)
            db.session.commit()
            return owner
        except IntegrityError:
            raise ValueError("owner already exists")
        
    # def __init__(self, first_name, last_name, email, password):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.password = generate_password_hash(password)

    def check_password(self, password_to_check):
        return check_password_hash(self.password, password_to_check)
