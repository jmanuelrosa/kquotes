import graphene

from graphene import Node

from graphene_django import DjangoObjectType

from django.contrib.auth import get_user_model

from kquotes.auth.jwt import settings as jwt_settings

generate_payload = jwt_settings.JWT_GENERATE_PAYLOAD_HANDLER
jwt_encode = jwt_settings.JWT_ENCODE_HANDLER


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

        payload = generate_payload(self)
        token = jwt_encode(payload)

        return token
