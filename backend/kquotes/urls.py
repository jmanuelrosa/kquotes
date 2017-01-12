from django.conf.urls import url
from django.contrib import admin

from .schema import schema
from .views import AuthGraphQLView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', AuthGraphQLView.as_view(graphiql=True, schema=schema)),
]
