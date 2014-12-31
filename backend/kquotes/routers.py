from kquotes.base.api import routers

router = routers.DefaultRouter()

from kquotes.users.api import UsersViewSet
router.register(r'users', UsersViewSet)

from kquotes.organizations.api import OrganizationsViewSet
from kquotes.organizations.api import MembersViewSet
router.register(r'organizations', OrganizationsViewSet)
router.register(r'members', MembersViewSet)

from kquotes.quotes.api import QuotesViewSet
router.register(r'quotes', QuotesViewSet)
