from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_marshmallow import Marshmallow
import os
import datetime
import json

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


#Model
class Car(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    make = db.Column(db.String(80), unique = False)
    model = db.Column(db.String(80), unique = False)
    year = db.Column(db.Integer)
    chasis_id = db.Column(db.String(80))
    price = db.Column(db.Integer)

    def __init__(self, make, model, year, chasis_id, price):
        self.make = make
        self.model = model
        self.year = year
        self.chasis_id = chasis_id
        self.price = price

    def serialize(self):
        return json.dumps({
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'chasis_id': self.chasis_id,
            'price': self.price,
            })
    
    @staticmethod
    def car_from_json(json_data):
        data = json.loads(json_data)
        make = data.get('make')
        model = data.get('model')
        year = data.get('year')
        chasis_id = data.get('chasis_id')
        price = data.get('price')
        return Car(make, model, year, chasis_id, price)

    def output(self):
        data = {
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'chasis_id': self.chasis_id,
            'price': self.price,
        }
        return json.dumps(data)

#Schema
class CarSchema(ma.Schema):
    class Meta:
        # Fields to expose, do not expost the chasis_id
        fields = ('make', 'model', 'year', 'price')

car_schema = CarSchema()
cars_schema = CarSchema(many=True)

#Show all cars
@app.route("/cars", methods=["GET"])
def get_cars():
    all_cars = Car.query.all()
    res = cars_schema.dump(all_cars)
    return jsonify(res.data)

#Show car by id
@app.route("/cars/<id>", methods=["GET"])
def get_car(id):
    car = Car.query.get(id)
    return car_schema.jsonify(car) #Single result - not iterable

#Create new car
@app.route("/car", methods=["POST"])
def create_car():
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    chasis_id = request.json['chasis_id']
    price = request.json['price']
    
    new_car = Car(make, model, year, chasis_id, price)

    db.session.add(new_car)
    db.session.commit()

    json_car = new_car.serialize()
    car_back = Car.car_from_json(json_car)
    return car_back.output()

#Get average price
@app.route("/avg", methods=["POST"])
def get_average():
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    average_price = db.session.query(func.avg(Car.price)).filter(Car.make == make).filter(Car.model == model).filter(Car.year == year).scalar()

    data = {
        'average_price': average_price
    }

    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)