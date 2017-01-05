import graphene
from graphene import AbstractType, Mutation, Node

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Quote
from .models import Score


class QuoteNode(DjangoObjectType):
    class Meta:
        model = Quote
        interfaces = (Node, )


class ScoreNode(DjangoObjectType):
    class Meta:
        model = Score


class QuotesQuery(AbstractType):
    quote = graphene.Field(QuoteNode)
    quotes = DjangoFilterConnectionField(QuoteNode)


class QuotesMutation(AbstractType):
    pass
