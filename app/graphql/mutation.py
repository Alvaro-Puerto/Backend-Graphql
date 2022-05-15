import graphene
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.model import Car, User
from app.graphql.objects import CarType, UserType


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

class UserCreateMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(lambda: UserType)

    def mutate(self, info, username, password, email):
        user = User(
                        username=username, 
                        password=generate_password_hash(password),
                        email=email
                    )
        
        db.session.add(user)
        db.session.commit()

        return UserCreateMutation(user=user)

class Mutation(graphene.ObjectType):
    car_add_mutation = CarCreateMutation.Field()
    car_edit_mutation = CarUpdateMutation.Field()
    car_delete_mutation = CarDeleteMutation.Field()
    user_create_mutation = UserCreateMutation.Field()