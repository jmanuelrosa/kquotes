from django.core.management.base import BaseCommand
from django.db import transaction
from django.conf import settings

from sampledatahelper.helper import SampleDataHelper

from kquotes.users.models import User
from kquotes.quotes.models import Quote
from kquotes.quotes.models import Score


SD = SampleDataHelper(seed=12345678901)


####################################################
## Users
####################################################

def create_user(username, email, first_name=None, last_name=None, is_admin=False):
    user = User(username=username,
                email=email,
                first_name=first_name or SD.name(),
                last_name=last_name or SD.surname(),
                is_admin=is_admin,
                is_active=True)

    user.set_password(123123)
    user.save()

    if is_admin:
        print ("- Create superuser: {}".format(user))
    else:
        print ("- Create user: {}".format(user))

    return user


####################################################
## Quotes
####################################################

def create_quote(author=None):
    quote = Quote(quote=SD.paragraph(),
                  explanation=SD.paragraph(),
                  creator=SD.db_object_from_queryset(User.objects.exclude(is_admin=True)))

    if author:
        quote.author = author
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
        create_user('admin', 'admin@kquotes.com', 'David', 'Barragán', is_admin=True)

        # Create Users
        users = [('user{}'.format(i), "user{}@kquotes.com".format(i)) for i in range(25)]
        for username, email in users:
            user = create_user(username, email)

            # Create quotes
            for i in range(0, 20 + SD.int(max_value=80)):
                create_quote(user)

        # Create quotes without author
        for i in range(0, 20 + SD.int(max_value=80)):
            create_quote()
