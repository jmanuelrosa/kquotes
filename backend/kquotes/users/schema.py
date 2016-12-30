from graphene import relay, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from . import models


class UserNode(DjangoObjectType):
    class Meta:
        model = models.User
        filter_fields = {
            'username': ['exact',],
            'email': ['exact', 'iexact'],
        }
        interfaces = (relay.Node,)


class UsersQuery(AbstractType):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
