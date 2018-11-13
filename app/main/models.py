# your models live here

# this is what you need to implement an Array Column
from sqlalchemy.dialects import postgresql
# Column Type: postgresql.ARRAY(db.Integer)
import enum
from app.authentification.models import Owner
from flask import url_for


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

    def __repr__(self):
        return '<Text {}: {}>'.format(self.id, self.title)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180), nullable=False)
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
    texts = db.relationship('Text', backref='restaurant',lazy=True)

    def __repr__(self):
        return '<Restaurant {}: {}>'.format(self.id, self.name) 

    def set_active_text(self, text):
        self.text_active = text.id

    def _get_menu(self):
        return MenuParagraph.query.filter_by(restaurant_id = self.id).join(Dish).join(DishVariant, Dish.id == DishVariant.dish_id).all()
        
        # MenuParagraph.query.join(Dish, Dish.menuparagraph_id == MenuParagraph.id).filter_by(restaurant_id = 1).add_columns(Dish.name, Dish.price, Dish.description).all()
    def _get_menu_dict(self):
        paragraphs = self._get_menu()
        data = {
        }
        for paragraph in paragraphs:
            if paragraph.title not in data:
                data[paragraph.title] = []
            for dish in paragraph.dishes:
                data[paragraph.title].append(dish.to_dict())
        return data



    def to_dict(self):
        data = {
            'id' : self.id,
            'name' : self.name,
            'contact' : {
                'email' : self.email,
                'telephone' : self.telephone,
                'street' : self.street,
                'street_number' : self.street_number,
                'city_code' : self.city_code,
                'city' : self.city,
            },
            'content' : {
                'text_active' : self.text_active,
            },
            'menu' : self._get_menu_dict(),
            '_links' : 
                {
                    'self' : url_for('api.get_restaurant', id=self.id),
                }
            
        }
        return data
    
    @staticmethod
    def collection_dict():
        resources = Restaurant.query.all()
        data = {
            # 'items' : [item.to_dict() for item in resources],
            '_meta' : {
                'total_items' : resources.items(), 
            }
        }
        return data
        
            

    def from_dict(self, data):
        for field in ["name", "email", "telephone", "street", "street_number", "city_code", "city"]:
            if field in data:
                setattr(self, field, data[field])


def myconverter(o):

    if isinstance(o, datetime):
        return o.__str__()
    else:
        return o.__dict__


class MenuParagraph(db.Model):
    __tablename__ = 'menuparagraph'

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
    vegetarian = db.Column(db.Boolean(), nullable=False, default=False)
    vegan = db.Column(db.Boolean(), nullable=False, default= False)
    allergens = db.Column(postgresql.ARRAY(db.Enum(AllergenType)), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    menuparagraph_id = db.Column(db.Integer, db.ForeignKey('menuparagraph.id'), nullable=True)

    variants = db.relationship('DishVariant', backref='dish',lazy='joined')

    def to_dict(self):
        data = {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description,
            "variants" : []
        }
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

    def to_dict(self):
        data = {
            "measurement" : self.measurement,
            "price" : str(self.price),
            "id" : self.id
        }
        return data

    def __repr__(self):
        return '<Dish {}: DishVariant {}>'.format(self.dish_id, self.id)




