from django.conf.urls import include, url
from django.contrib import admin

from .routers import router

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/auth/token', 'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^admin/', include(admin.site.urls)),
]



from django.conf import settings

if settings.DEBUG:
    # Hardcoded only for development server
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns(prefix="/static/")

    def mediafiles_urlpatterns(prefix):
        """
        Method for serve media files with runserver.
        """
        import re
        from django.views.static import serve

        return [url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), serve,
                    {'document_root': settings.MEDIA_ROOT})]
    urlpatterns += mediafiles_urlpatterns(prefix="/media/")
