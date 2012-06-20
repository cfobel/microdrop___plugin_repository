from jsonrpc import jsonrpc_method


@jsonrpc_method('repository.api_version')
def api_version(request):
    return {'major': 0, 'minor': 1, 'micro': 0}


@jsonrpc_method('repository.available_plugins')
def available_plugins(request):
    return ['microdrop.plugins.dmf_control_board', 
            'microdrop.plugins.test_plugin',]


@jsonrpc_method('repository.plugin_info')
def plugin_info(request, plugin_name):
    return {'name': plugin_name, 'version': '0.1.232'}


@jsonrpc_method('repository.plugin_url')
def plugin_url(request, plugin_name, version):
    return 'http://link.to.some.plugin/%s/%s' % (plugin_name, version)
