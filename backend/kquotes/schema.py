import graphene

from .users.schema import UsersQuery, UsersMutation
from .quotes.schema import QuotesQuery, QuotesMutation
#from .memes.schema import MemesQuery, MemesMutation


class Query(UsersQuery,
            QuotesQuery,
            #MemesQuery,
            graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(UsersMutation,
               QuotesMutation,
               #MemesMutation,
               graphene.ObjectType):
    # This class will inherit from multiple Mutations
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
