import graphene
from graphene import AbstractType

from graphene_django.filter import DjangoFilterConnectionField

from .mutations import RegisterUser
from .mutations import LoginUser
from .mutations import ResetPasswordRequest
from .mutations import ResetPassword
from .mutations import UpdateUser

from .nodes import UserNode


class UsersQuery(AbstractType):
    me = graphene.Field(UserNode)
    user = graphene.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)

    def resolve_me(self, args, context, info):
        return UserNode.get_node(context.user.id, context, info)


class UsersMutation(AbstractType):
    #register_user = RegisterUser.Field()
    login_user = LoginUser.Field()
    reset_password_request = ResetPasswordRequest.Field()
    reset_password = ResetPassword.Field()
    update_user = UpdateUser.Field()
