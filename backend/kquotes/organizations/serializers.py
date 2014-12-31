from kquotes.base.api import serializers

from . import models


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
