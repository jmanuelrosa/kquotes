import graphene
from graphene import AbstractType

from graphene_django.filter import DjangoFilterConnectionField

from kquotes.auth.decorators import login_required

from .models import Quote
from .nodes import QuoteNode


class QuotesQuery(AbstractType):
    quote = graphene.Field(QuoteNode)
    quotes = DjangoFilterConnectionField(QuoteNode)

    @login_required
    def resolve_quote(self, args, context, info):
        return Quote.objects.all()

    @login_required
    def resolve_quotes(self, args, context, info):
        return Quote.objects.all()
