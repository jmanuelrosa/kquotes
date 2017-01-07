import graphene
from graphene import relay

from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode as uid_decoder

from .models import Quote

from .nodes import QuoteNode


class AddQuote(relay.ClientIDMutation):
    ok = graphene.Boolean()
    result = graphene.Field(QuoteNode)

    class Input:
        quote = graphene.String(required=True)
        explanation = graphene.String()
        author = graphene.ID()
        external_author =  graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        quote = Quote(quote=input.get('quote'),
                      explanation=input.get('explanation'),
                      creator=context.user)

        author_uuid = input.get('author', None)
        external_author = input.get('external_author', None)
        if author_uuid:
            try:
                id = force_text(uid_decoder(author_uuid))
                quote.author = get_user_model.objects.get(id=id)
            except (TypeError, ValueError, OverflowError):
                raise Exception("'author'(ID) must be a valid user ID")
            except get_user_model.DoesNotExist:
                raise Exception("there is no user with this ID")
        elif external_author:
            quote.external_author = external_author
        else:
            raise Exception("you need tu set an 'author' (ID) or an 'external autor' (String)")

        quote.save()

        return AddQuote(ok=True, quote=quote)
