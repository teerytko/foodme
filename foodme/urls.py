import os.path
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

from oscar.app import application

urlpatterns = [
    # Examples:
    # url(r'^$', 'foodme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(application.urls)),
]

if settings.DEBUG: # this is set to True in my settings.py
    urlpatterns += patterns("",
        url(r"^%s(?P<path>.*)$" % settings.MEDIA_URL[1:],
            "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}))
