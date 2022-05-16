import graphene
from graphql_relay.node.node import from_global_id
from werkzeug.security import generate_password_hash, check_password_hash
from flask_graphql_auth import create_access_token, create_refresh_token, mutation_jwt_required
from app import db
from app.model import Car, User
from app.graphql.objects import CarType, UserType


class CarCreateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        brand = graphene.String(required=True)
        model = graphene.String(required=True)
        color = graphene.String(required=True)
        price = graphene.String(required=True)
        year = graphene.String(required=True)

    
    car = graphene.Field(lambda: CarType)

    def mutate(self, info, brand, model, color, price, year):
        car = Car(
                    brand= brand, 
                    model= model, 
                    color= color,
                    price= float(price),
                    year= int(year) 
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
        price = graphene.String(required=True)
        year = graphene.String(required=True)

    car = graphene.Field(lambda: CarType)

    def mutate(self, info,id ,brand, model, color, price, year):
        id = from_global_id(id)
        car = Car.query.filter_by(id=id[1]).first()
       
        if car:
            car.brand = brand
            car.model = model
            car.year = int(year)
            car.color = color
            car.price = float(price)
            db.session.commit()

        return CarCreateMutation(car=car)

class CarDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    car = graphene.Field(lambda: CarType)
    
    def mutate(self, info, id):
        id = from_global_id(id)
        print(id)
        Car.query.filter_by(id=id[1]).delete()

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

class AuthMutation(graphene.Mutation):
    access_token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        email = graphene.String()
        password = graphene.String()
    
    def mutate(self, info , email, password) :
        user = User.query.filter_by(email=email).first()
        print(user)
        if not user:
            raise Exception('Authenication Failure : Usuario registrado')

        if check_password_hash(user.password, password):
            return AuthMutation(
                access_token = create_access_token(email),
                refresh_token = create_refresh_token(email)
            )
        else:
            raise Exception('Authenication Failure : Contraseña incorrecta')


class Mutation(graphene.ObjectType):
    car_add_mutation = CarCreateMutation.Field()
    car_edit_mutation = CarUpdateMutation.Field()
    car_delete_mutation = CarDeleteMutation.Field()
    user_create_mutation = UserCreateMutation.Field()
    auth_mutation = AuthMutation.Field()