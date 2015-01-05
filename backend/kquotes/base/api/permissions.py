# -*- coding: utf-8 -*-
from rest_framework import permissions


class AllowAny(permissions.AllowAny):
    pass

class IsAuthenticated(permissions.IsAuthenticated):
    pass
