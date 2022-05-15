from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.model import Car, User

class CarType(SQLAlchemyObjectType):
    class Meta:
        model = Car 
        interfaces = (relay.Node,)


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)
