# your models live here

# this is what you need to implement an Array Column
from sqlalchemy.dialects import postgresql
# Column Type: postgresql.ARRAY(db.Integer)

from app.authentification.models import Owner


from app import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    email = db.Column(db.String(120))
    telephone = db.Column(db.String(40))
    street = db.Column(db.String(180))
    street_number = db.Column(db.String(20))
    city_code = db.Column(db.String(20))
    city = db.Column(db.String(120))
    text_active = db.Column(postgresql.ARRAY(db.Integer))
    menu_paragraphs = db.relationship('Menu_Paragraph', backref='restaurant',lazy='joined')
    dishes = db.relationship('Dish', backref='restaurant',lazy='True')

    def __repr__(self):
        return '<Restaurant {}: {}>'.format(self.id, self.name) 


class Menu_Paragraph(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    dishes = db.relationship('Dish', backref='menu_paragraph',lazy='joined')

    def __repr__(self):
        return '<Menu Paragraph {}: {}>'.format(self.id, self.title)

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable = False)
    description = db.Column(db.String(200), nullable = True)
    vegetarian = db.Column(db.Boolean, default=False)
    vegan = db.Column(db.Boolean(), default= False)
    measurement = db.Column(db.String(120), nullable=True)
    price = db.Column(db.Numeric(10,2), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    menuparagraph_id = db.Column(db.Integer, db.ForeignKey('menu__paragraph.id'), nullable=False)

    def __repr__(self):
        return '<Dish {}: {}>'.format(self.id, self.name)