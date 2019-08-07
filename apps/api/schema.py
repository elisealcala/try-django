import graphene
from account.schema import AccountQuery

class Query(AccountQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

# class Mutation(django_graphql_movies.movies.schema.Mutation, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    # pass

schema = graphene.Schema(query=Query)