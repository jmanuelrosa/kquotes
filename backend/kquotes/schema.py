import graphene

from .users.queries import UsersQuery
from .users.mutations import UsersMutation

from .quotes.queries import QuotesQuery
from .quotes.mutations import QuotesMutation

#from .memes.queries import MemesQuery
#from .memes.mutations import MemesMutation


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
