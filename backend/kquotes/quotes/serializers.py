from kquotes.base.api import serializers
from kquotes.users.serializers import UserInfoSerializer

from . import models


class QuoteSerializer(serializers.ModelSerializer):
    author_user = serializers.SerializerMethodField()
    creator_user = serializers.SerializerMethodField()

    class Meta:
        model = models.Quote

    def get_author_user(self, obj):
        if obj.author:
            return UserInfoSerializer(obj.author).data
        return None

    def get_creator_user(self, obj):
        if obj.creator:
            return UserInfoSerializer(obj.creator).data
        return None
