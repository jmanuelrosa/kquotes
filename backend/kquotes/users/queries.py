import graphene
from graphene import AbstractType

from graphene_django.filter import DjangoFilterConnectionField

from django.contrib.auth import get_user_model
from kquotes.auth.decorators import login_required

from .nodes import UserNode


class UsersQuery(AbstractType):
    me = graphene.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)

    @login_required
    def resolve_me(self, args, context, info):
        return UserNode.get_node(context.user.id, context, info)

    @login_required
    def resolve_users(self, args, context, info):
        return get_user_model().objects.filter(is_active=True)
