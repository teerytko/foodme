from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    url(r'^$', 'shop.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]



if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
