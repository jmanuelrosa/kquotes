from kquotes.base.api import viewsets
from . import models
from . import serializers


class QuotesViewSet(viewsets.ModelCrudViewSet):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer
