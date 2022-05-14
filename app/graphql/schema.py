import graphene
from app.graphql.mutation import Mutation
from app.graphql.query import Query
schema = graphene.Schema(mutation=Mutation, query=Query)
