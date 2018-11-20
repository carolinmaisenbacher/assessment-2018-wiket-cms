# your models live here

# this is what you need to implement an Array Column
from sqlalchemy.dialects import postgresql
# Column Type: postgresql.ARRAY(db.Integer)
import enum
from app.authentification.models import Owner
from flask import url_for
import html

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
    text = db.Column(postgresql.TEXT(), nullable=False)
    created = db.Column(db.DateTime(), default=datetime.utcnow)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    texts_active = db.relationship('TextActive', backref=db.backref('text', lazy='joined'),lazy=True)

    def to_dict(self):
        data = {
            'id' : self.id,
            'title' : html.unescape(self.title),
            'text' : html.unescape(self.text),
            'created' : self.created
        }
        return data

    def __repr__(self):
        return '<Text {}: {}>'.format(self.id, self.title)

class TextActive(db.Model):
    position = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), primary_key=True, nullable=False)
    text_id = db.Column(db.Integer, db.ForeignKey('text.id'), primary_key=True, nullable=False)

    def to_dict(self):
        return self.text.to_dict()

    def __repr__(self):
        return '<Active Text {}: {}>'.format(self.id, self.text.title)

    def __lt__(self, other):
        if self.position < other.position:
            return True
        return False

    def __gt__(self, other):
        if self.position > other.position:
            return True
        return False


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    telephone = db.Column(db.String(40), nullable=True)
    street = db.Column(db.String(180), nullable=False)
    street_number = db.Column(db.String(20), nullable=True)
    city_code = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    # texts_active = db.relationship('Text', secondary=texts_active, lazy='joined', backref=db.backref('pages', lazy=True))

    menu_paragraphs = db.relationship('MenuParagraph', backref='restaurant',lazy='joined')
    dishes = db.relationship('Dish', backref='restaurant',lazy=True)
    texts = db.relationship('Text', backref='restaurant',lazy=True)
    texts_active = db.relationship('TextActive', backref=db.backref('restaurant', lazy=True),lazy='joined')

    def __repr__(self):
        return '<Restaurant {}: {}>'.format(self.id, self.name) 

    def _menu_to_sorted_array(self):
        self.menu_paragraphs.sort()
        return [paragraph.to_dict() for paragraph in self.menu_paragraphs]

    def _active_texts_to_sorted_array(self):
        self.texts_active.sort()
        return [text.to_dict() for text in self.texts_active]

    def to_dict(self):
        
        data = {
            'id' : self.id,
            'name' : html.unescape(self.name),
            'contact' : self._contact_to_dict(),
            'content' : {
                'texts' : self._active_texts_to_sorted_array()
            },
            'menu' : self._menu_to_sorted_array(),
            '_links' : 
                {
                    'self' : url_for('api.get_restaurant', id=self.id),
                }   
            
        }
        return data

    def _contact_to_dict(self):
        data = {
            'street' : html.unescape(self.street),
            'city_code' : html.unescape(self.city_code),
            'city' : html.unescape(self.city),
        }
        if self.email:
            data['email'] = html.unescape(self.email)
        if self.telephone:
            data['telephone'] = html.unescape(self.telephone)
        if self.street_number:
            data['street_number'] = html.unescape(self.street_number)
        return data


    @staticmethod
    def collection_dict():
        restaurants = Restaurant.query.all()
        data = {
            'restaurants' : [restaurant.to_dict() for restaurant in restaurants],
            '_meta' : {
                'total_items' : len(restaurants), 
            }
        }
        return data

    def from_dict(self, data):
        for field in ["name", "email", "telephone", "street", "street_number", "city_code", "city"]:
            if field in data:
                setattr(self, field, data[field])

class MenuParagraph(db.Model):
    __tablename__ = 'menuparagraph'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    dishes = db.relationship('Dish', backref='menu_paragraph',lazy='joined')

    def to_dict(self):
        data = {    
            "id" : self.id,       
            "title" : self.title
        }
        if self.description:
            data["description"] = self.description         
        data["dishes"] = [dish.to_dict() for dish in self.dishes]
        return data

    def __repr__(self):
        return '<Menu Paragraph {}: {}>'.format(self.id, self.title)

    def __lt__(self, other):
        if self.position < other.position:
            return True
        return False

    def __gt__(self, other):
        if self.position > other.position:
            return True
        return False

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable = False)
    description = db.Column(db.String(200), nullable = True)
    vegetarian = db.Column(db.Boolean(), nullable=False, default=False)
    vegan = db.Column(db.Boolean(), nullable=False, default= False)
    allergens = db.Column(postgresql.ARRAY(db.Enum(AllergenType)), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    menuparagraph_id = db.Column(db.Integer, db.ForeignKey('menuparagraph.id'), nullable=True)
    position = db.Column(db.Integer, nullable=False)

    variants = db.relationship('DishVariant', backref='dish',lazy='joined')

    def to_dict(self):
        data = {
            "id" : self.id,
            "name" : html.unescape(self.name),
            "variants" : []
        }
        if self.description:
            data["description"] = html.unescape(self.description)

        for variant in self.variants:
            data["variants"].append(variant.to_dict())
        if self.vegan:
            data["vegan"] = True
        if self.vegetarian:
            data["vegetarian"] = True   
        return data

    def __repr__(self):
        return '<Dish {}: {}>'.format(self.id, self.name)

class DishVariant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    measurement = db.Column(db.String(120), nullable=True)
    price = db.Column(db.Numeric(10,2), nullable=True)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), nullable=False)
    position = db.Column(db.Integer, default=1)

    def to_dict(self):
        data = {
            "measurement" : html.unescape(str(self.measurement)),
            "price" : str(self.price),
            "id" : self.id
        }
        return data

    def __repr__(self):
        return '<Dish {}: DishVariant {}>'.format(self.dish_id, self.id)




