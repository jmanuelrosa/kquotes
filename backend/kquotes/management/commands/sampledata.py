from django.core.management.base import BaseCommand
from django.db import transaction
from django.conf import settings

from sampledatahelper.helper import SampleDataHelper

from kquotes.users.models import User
from kquotes.organizations.models import Organization
from kquotes.organizations.models import Member
from kquotes.quotes.models import Quote
from kquotes.quotes.models import Score


SD = SampleDataHelper(seed=12345678901)

BASE_USERS = getattr(settings, "SAMPLEDATA_BASE_USERS", [])
BASE_ORGANIZATIONS = getattr(settings, "SAMPLEDATA_BASE_ORGANIZATIONS", [])


####################################################
## Users
####################################################

def create_superuser():
    user, created = User.objects.get_or_create(username="admin",
                                               email="admin@kquotes.com",
                                               is_superuser=True)

    if created:
        user.set_password(123123)
        user.save()
        print ("- Create superuser: {}".format(user))

    return user


def create_user(username=None, email=None, full_name=None):
    user = User(username=username,
                email=email,
                full_name=full_name,
                is_superuser=False)
    user.set_password(123123)
    user.save()

    print ("- Create user: {}".format(user))
    return user


####################################################
## Organizations
####################################################

def create_organization(name=None):
    org = Organization(name=name)
    org.save()

    print("- Create organization: {}".format(org))
    return org


def create_member(org, user, is_owner=False, is_admin=False):
    member = Member(user=user,
                    organization=org,
                    is_owner=is_owner,
                    is_admin=is_admin)
    member.save()

    print("- Create member: {}".format(member))
    return member


####################################################
## Quotes
####################################################

def create_quote(org):
    quote = Quote(quote=SD.paragraph(),
                  explanation=SD.paragraph(),
                  creator=SD.db_object_from_queryset(org.members).user,
                  organization=org)
    if SD.boolean():
        quote.author = SD.db_object_from_queryset(org.members).user
    else:
        quote.external_author = SD.words(2, 3)
    quote.save()

    print("- Create quote: #{}".format(quote.id))
    return quote


####################################################
## MAIN COMMAND
####################################################

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        # Create superuser
        create_superuser()

        # Create Users
        users = [create_user(**user) for user in BASE_USERS]

        # Create organizations
        orgs = [create_organization(**org) for org in BASE_ORGANIZATIONS]
        for org in orgs:
            # Create owner
            owner = SD.db_object(User)
            create_member(org, owner, is_owner=True, is_admin=True)

            # Create members
            for user in User.objects.exclude(id=owner.id)[:SD.int(1, User.objects.all().count())]:
                create_member(org, user, is_owner=SD.boolean(), is_admin=SD.boolean())

            # Create quotes
            for i in range(0, 20 + SD.int(max_value=80)):
                create_quote(org)
