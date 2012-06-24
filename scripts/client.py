import sys

from path import path
from django.core.exceptions import ObjectDoesNotExist

project_root = path(__file__).parent.parent
sys.path.append(project_root)

from repository.models import PluginVersion, Plugin, cre_plugin_info


def process_plugin_archive(plugin_path):
    match = cre_plugin_info.match(plugin_path.name)
    if match:
        major, minor, micro = int(match.group('major')),\
                int(match.group('minor')), int(match.group('micro'))

        plugin, created = Plugin.objects.get_or_create(name=match.group(
                'name'))
        plugin_version, created = PluginVersion.objects.get_or_create(
                plugin=plugin, major=major, minor=minor, micro=micro)
        if created:
            print 'Added Plugin %s version %s.%s.%s' % (plugin.name, 
                    plugin_version.major, plugin_version.minor,
                            plugin_version.micro)


def scan_for_plugins(plugins_path):
    plugin_files = plugins_path.files('*.tar.gz')

    for plugin_path in plugin_files:
        process_plugin_archive(plugin_path)


if __name__ == '__main__':
    project_root = path(__file__).parent.parent
    scan_for_plugins(project_root.joinpath('plugin_data'))
