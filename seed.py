import pandas
from app import Car, db


# Seed method to add some initial data
def seed():
    df = pandas.read_table("data/data.csv", sep=",")

    for index, row in df.iterrows():
        make = row[0]
        model = row[1]
        year = row[2]
        chasis_id = row[3]
        price = row[4]
        last_updated = row[5]

        new_car = Car(make, model, year, chasis_id, price)
        db.session.add(new_car)
        db.session.commit()

seed()
