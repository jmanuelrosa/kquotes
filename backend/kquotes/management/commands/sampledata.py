from django.core.management.base import BaseCommand
from django.db import transaction
from django.conf import settings

from sampledatahelper.helper import SampleDataHelper

from kquotes.users.models import User
from kquotes.organizations.models import Organization
from kquotes.organizations.models import Member


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
        print ("- Create superuser: ", user)

    return user


def create_user(username=None, email=None, full_name=None):
    user = User(username=username,
                email=email,
                full_name=full_name,
                is_superuser=False)
    user.set_password(123123)
    user.save()

    print ("- Create user: ", user)
    return user


####################################################
## Organizations
####################################################

def create_organization(name=None):
    org = Organization(name=name)
    org.save()

    print("- Create organization: ", org)
    return org


def create_member(org, user, is_owner=False, is_admin=False):
    member = Member(user=user,
                    organization=org,
                    is_owner=is_owner,
                    is_admin=is_admin)
    member.save()

    print("- Create member: ", member)
    return member


####################################################
## MAIN COMMAND
####################################################

SD = SampleDataHelper(seed=12345678901)

BASE_USERS = getattr(settings, "SAMPLEDATA_BASE_USERS", [])
BASE_ORGANIZATIONS = getattr(settings, "SAMPLEDATA_BASE_ORGANIZATIONS", [])

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        create_superuser()

        # Create Users
        users = [create_user(**user) for user in BASE_USERS]

        # Create organizations
        orgs = [create_organization(**org) for org in BASE_ORGANIZATIONS]
        for org in orgs:
            owner = SD.db_object(User)
            create_member(org, owner, is_owner=True, is_admin=True)

            for user in User.objects.exclude(id=owner.id)[:SD.int(1, User.objects.all().count())]:
                create_member(org, user, is_owner=SD.boolean(), is_admin=SD.boolean())
