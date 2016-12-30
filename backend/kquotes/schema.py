import graphene

from .users.schema import UsersQuery
#from .quotes.schema import QuotesQuery
#from .memes.schema import MemesQuery


class Query(UsersQuery,
            #QuotesQuery,
            #MemesQuery,
            graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
