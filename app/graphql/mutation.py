import graphene
from pkg_resources import require
from app import db
from app.model import Car
from app.graphql.objects import CarType


class CarCreateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        brand = graphene.String(required=True)
        model = graphene.String(required=True)
        color = graphene.String(required=True)
        price = graphene.Float(required=True)
        year = graphene.Int(required=True)
    
    car = graphene.Field(lambda: CarType)

    def mutate(self, info, brand, model, color, price, year):
        car = Car(
                    brand= brand, 
                    model= model, 
                    color= color,
                    price= price,
                    year= year 
                )

        db.session.add(car)
        db.session.commit()

        return CarCreateMutation(car=car)

class CarUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        brand = graphene.String(required=True)
        model = graphene.String(required=True)
        color = graphene.String(required=True)
        price = graphene.Float(required=True)
        year = graphene.Int(required=True)

    car = graphene.Field(lambda: CarType)

    def mutate(self, info,id ,brand, model, color, price, year):
        car = Car.query.filter_by(id=id).first()
        print(id)
        if car:
            car.brand = brand
            car.model = model
            car.year = year
            car.color = color
            car.price = price
            db.session.commit()

        return CarCreateMutation(car=car)

class CarDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    car = graphene.Field(lambda: CarType)

    def mutate(self, info, id):
        Car.query.filter_by(id=id).delete()

        db.session.commit()

        return None

class Mutation(graphene.ObjectType):
    car_add_mutation = CarCreateMutation.Field()
    car_edit_mutation = CarUpdateMutation.Field()
    car_delete_mutation = CarDeleteMutation.Field()