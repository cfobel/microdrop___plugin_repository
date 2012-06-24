from django.conf.urls.defaults import *
from django_jsonrpc import jsonrpc_site

import repository.views
from repository.models import PluginVersion, Plugin
import repository.app_settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()
admin.site.register(PluginVersion)
admin.site.register(Plugin)

urlpatterns = patterns('',
    # Example:
    # (r'^plugin_repository/', include('plugin_repository.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    url(r'^json/browse/$', 'django_jsonrpc.views.browse', name='jsonrpc_browser'),
    url(r'^json/$', jsonrpc_site.dispatch, name='jsonrpc_mountpoint'),
    (r'^json/(?P<method>[a-zA-Z0-9.-_]+)$', jsonrpc_site.dispatch),
    (r'^plugin_data/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': repository.app_settings.PLUGIN_DATA_DIR,
                    'show_indexes': True}),
)
