from django_jsonrpc import jsonrpc_method
from .models import Plugin, PluginVersion


@jsonrpc_method('repository.api_version')
def api_version(request):
    return {'major': 0, 'minor': 1, 'micro': 0}


@jsonrpc_method('repository.available_plugins')
def available_plugins(request):
    return [p.name for p in Plugin.objects.order_by('name')]


@jsonrpc_method('repository.plugin_latest_version')
def plugin_latest_version(request, plugin_name):
    plugin_version = PluginVersion.objects.filter(plugin__name=plugin_name
            ).order_by('-major', '-minor', '-micro')[0]
    return {'major': plugin_version.major, 'minor': plugin_version.minor,
            'micro': plugin_version.micro}


@jsonrpc_method('repository.plugin_versions')
def plugin_versions(request, plugin_name):
    plugin_versions = PluginVersion.objects.filter(plugin__name=plugin_name
            ).order_by('major', 'minor', 'micro')
    return [{'major': version.major, 'minor': version.minor,
            'micro': version.micro} for version in plugin_versions]


@jsonrpc_method('repository.plugin_url')
def plugin_url(request, plugin_name, version):
    plugin_version = PluginVersion.objects.get(plugin__name=plugin_name,
            major=version['major'], minor=version['minor'],
                    micro=version['micro'])
    return str(plugin_version.url())
