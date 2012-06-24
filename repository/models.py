import re

from django.db import models
from path import path

import app_settings


cre_plugin_info = re.compile(r'''
        (?P<name>[a-zA-Z_]+)-
        (?P<major>\d+)\.(?P<minor>\d+)\.(?P<micro>\d+)
        \.tar\.gz''', re.VERBOSE)


class PluginVersion(models.Model):
    major = models.IntegerField()
    minor = models.IntegerField()
    micro = models.IntegerField()
    plugin = models.ForeignKey('Plugin')

    def url(self):
        plugin_path = self.path()
        plugin_url = path(app_settings.PLUGIN_DATA_URL)
        return plugin_url.joinpath(plugin_path.name)

    def path(self):
        plugin_data_dir = path(app_settings.PLUGIN_DATA_DIR)
        plugin_filename = '%s-%s.%s.%s.tar.gz' % (self.plugin.name, self.major,
                self.minor, self.micro)
        plugin_path = plugin_data_dir.joinpath(plugin_filename)

        if not plugin_path.isfile():
            raise ValueError, 'Plugin not found: %s'
        else:
            return plugin_path


class Plugin(models.Model):
    name = models.CharField(max_length=200)
