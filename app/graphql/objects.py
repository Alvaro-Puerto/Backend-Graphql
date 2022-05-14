from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.model import Car

class CarType(SQLAlchemyObjectType):
    class Meta:
        model = Car 
        interfaces = (relay.Node,)

