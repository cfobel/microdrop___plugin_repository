from django.conf.urls.defaults import *
from jsonrpc import jsonrpc_site

import repository.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^plugin_repository/', include('plugin_repository.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    url(r'^json/browse/$', 'jsonrpc.views.browse', name='jsonrpc_browser'),
    url(r'^json/$', jsonrpc_site.dispatch, name='jsonrpc_mountpoint'),
    (r'^json/(?P<method>[a-zA-Z0-9.-_]+)$', jsonrpc_site.dispatch),
)
