from graphene_django.views import GraphQLView

from kquotes.auth.jwt.mixins import JSONWebTokenAuthMixin


class AuthGraphQLView(JSONWebTokenAuthMixin, GraphQLView):
    pass

