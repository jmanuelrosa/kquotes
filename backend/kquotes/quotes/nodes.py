from graphene import Node
from graphene_django import DjangoObjectType

from .models import Quote
from .models import Score


class QuoteNode(DjangoObjectType):
    class Meta:
        model = Quote
        interfaces = (Node, )


class ScoreNode(DjangoObjectType):
    class Meta:
        model = Score
