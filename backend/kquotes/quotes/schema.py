import graphene
from graphene import AbstractType

from graphene_django.filter import DjangoFilterConnectionField

from .nodes import QuoteNode
from .mutations import AddQuote


class QuotesQuery(AbstractType):
    quote = graphene.Field(QuoteNode)
    quotes = DjangoFilterConnectionField(QuoteNode)


class QuotesMutation(AbstractType):
    add_quote = AddQuote.Field()
