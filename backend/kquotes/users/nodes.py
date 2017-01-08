import graphene

from graphene import Node

from graphene_django import DjangoObjectType

from django.contrib.auth import get_user_model

from .auth import jwt


class UserNode(DjangoObjectType):
    token = graphene.String()
    is_current_user = False

    class Meta:
        model = get_user_model()
        interfaces = (Node, )
        only_fields = ('username', 'email', 'first_name', 'last_name',)

    @classmethod
    def get_node(cls, id, context, info):
        if context.user.id and user.id == context.user.id:
            return super().get_node(id, context, info)
        return None

    def resolve_token(self, args, context, info):
        if self.id != context.user.id and not self.is_current_user:
            return None

        payload = jwt.payload_handler(self)
        token = jwt.encode_handler(payload)

        return token
