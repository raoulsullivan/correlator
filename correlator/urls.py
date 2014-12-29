from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import EntryResource

entry_resource = EntryResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'correlator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'correlator.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(entry_resource.urls)),
)
