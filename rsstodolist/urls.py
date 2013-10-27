from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'', include('feeds.urls')),
)

urlpatterns += staticfiles_urlpatterns()
