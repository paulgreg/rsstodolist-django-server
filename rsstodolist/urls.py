from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#from feeds.models import FeedEntry

#admin.autodiscover()
#admin.site.register(FeedEntry)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rsstodolist.views.home', name='home'),

    url(r'', include('feeds.urls')),
    #url(r'^admin/', include(admin.site.urls))
)
