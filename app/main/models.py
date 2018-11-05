# your models live here

# this is what you need to implement an Array Column
from sqlalchemy.dialects import postgresql
# Column Type: postgresql.ARRAY(db.Integer)
import enum
from app.authentification.models import Owner


from app import db
from datetime import datetime

class AllergenType(enum.Enum):
    GLUTENHALTIGEGETREIDE = 1
    KREBSTIERE = 2
    EIER = 3
    FISCH = 4
    ERDNÜSSE = 5
    SOJABOHNEN = 6
    MILCH = 7
    SCHALENFRÜCHTE = 8
    SELLERIE = 9
    SENF = 10
    SESAMSAMEN = 11
    SCHWEFELDIOXIDSULFITE = 12
    LUPINEN = 13
    WEICHTIERE = 14

    def __repr__(self):
        return self.name

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False, default=str(id))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return '<Text {}: {}>'.format(self.id, self.title)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    email = db.Column(db.String(120))
    telephone = db.Column(db.String(40))
    street = db.Column(db.String(180))
    street_number = db.Column(db.String(20))
    city_code = db.Column(db.String(20))
    city = db.Column(db.String(120))
    text_active = db.Column(postgresql.ARRAY(db.Integer()), nullable=True)
    # text_active = db.Column(postgresql.ARRAY(db.Integer), nullable=True)

    menu_paragraphs = db.relationship('MenuParagraph', backref='restaurant',lazy='joined')
    dishes = db.relationship('Dish', backref='restaurant',lazy=True)
    dish_variants = db.relationship('DishVariant', backref='restaurant',lazy=True)
    texts = db.relationship('Text', backref='restaurant',lazy=True)

    def __repr__(self):
        return '<Restaurant {}: {}>'.format(self.id, self.name) 


class MenuParagraph(db.Model):
    __tablename__ = 'menuparagraph'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    dishes = db.relationship('Dish', backref='menu_paragraph',lazy='joined')
    dish_variants = db.relationship('DishVariant', backref='menu_paragraph',lazy=True)

    def __repr__(self):
        return '<Menu Paragraph {}: {}>'.format(self.id, self.title)

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable = False)
    description = db.Column(db.String(200), nullable = True)
    vegetarian = db.Column(db.Boolean(), default=False)
    vegan = db.Column(db.Boolean(), default= False)
    measurement = db.Column(db.String(120), nullable=True)
    price = db.Column(db.Numeric(10,2), nullable=True)
    allergens = db.Column(postgresql.ARRAY(db.Enum(AllergenType)), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    menu_paragraph_id = db.Column(db.Integer, db.ForeignKey('menuparagraph.id'), nullable=True)

    dish_variants = db.relationship('DishVariant', backref='dish',lazy='joined')

    def __repr__(self):
        return '<Dish {}: {}>'.format(self.id, self.name)

class DishVariant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    measurement = db.Column(db.String(120), nullable=True)
    price = db.Column(db.Numeric(10,2), nullable=True)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    menuparagraph_id = db.Column(db.Integer, db.ForeignKey('menuparagraph.id'), nullable=False)

    def __repr__(self):
        return '<Dish {}: {}>'.format(self.id, self.name)




