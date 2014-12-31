from kquotes.base.api import serializers

from . import models


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quote

