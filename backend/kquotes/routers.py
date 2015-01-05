from kquotes.base.api import routers

router = routers.DefaultRouter()

from kquotes.users.api import AuthTokenViewSet
router.register(r'auth/token', AuthTokenViewSet, base_name="auth")

from kquotes.users.api import UsersViewSet
router.register(r'users', UsersViewSet, base_name="users")

from kquotes.organizations.api import OrganizationsViewSet
from kquotes.organizations.api import MembersViewSet
router.register(r'organizations', OrganizationsViewSet, base_name="organizations")
router.register(r'members', MembersViewSet, base_name="members")

from kquotes.quotes.api import QuotesViewSet
router.register(r'quotes', QuotesViewSet, base_name="quotes")
