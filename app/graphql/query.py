import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from app.graphql.objects import CarType, UserType

class Query(graphene.ObjectType):
    relay = relay.Node.Field()
    
    cars = SQLAlchemyConnectionField(CarType)
    users = SQLAlchemyConnectionField(UserType)