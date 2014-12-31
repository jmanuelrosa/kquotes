from rest_framework.viewsets import ViewSetMixin
from rest_framework import views
from rest_framework import generics
from rest_framework import mixins

from . import pagination



class ViewSet(ViewSetMixin, views.APIView):
    """
    The base ViewSet class does not provide any actions by default.
    """
    pass


class GenericViewSet(ViewSetMixin, generics.GenericAPIView):
    """
    The GenericViewSet class does not provide any actions by default,
    but does include the base set of generic view behavior, such as
    the `get_object` and `get_queryset` methods.
    """
    pass

class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    """
    A viewset that provides default `list()` and `retrieve()` actions.
    """
    pass


class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass


#######################################################
## Extra ViewSets
#######################################################

class ReadOnlyListViewSet(pagination.HeadersPaginationMixin,
                          pagination.ConditionalPaginationMixin,
                          GenericViewSet):
    pass


class ModelListViewSet(pagination.HeadersPaginationMixin,
                       pagination.ConditionalPaginationMixin,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    pass


class ModelCrudViewSet(pagination.HeadersPaginationMixin,
                       pagination.ConditionalPaginationMixin,
                       ModelViewSet):
    pass
