import sys
import urllib

from path import path
from jsonrpc import ServiceProxy

project_root = path(__file__).parent.parent
sys.path.append(project_root)



def parse_args():
    """Parses arguments, returns ``(options, args)``."""
    from argparse import ArgumentParser

    parser = ArgumentParser(description="""\
Download latest version of specified plugin.""",
                           )
    parser.add_argument(nargs=1, dest='plugin_name', type=str)
    parser.add_argument(nargs=1, dest='output_dir', type=path)

    args = parser.parse_args()
    args.plugin_name = args.plugin_name[0]
    args.output_dir = args.output_dir[0]
    
    return args


def download_latest(plugin_name, output_dir):
    output_dir = path(output_dir)
    s = ServiceProxy('http://localhost:8000/json/')
    available_plugins = s.repository.available_plugins()
    if plugin_name not in available_plugins:
        raise ValueError, '''\
Plugin %s is not available.
Available plugins include: %s''' % (plugin_name, ', '.join(
                available_plugins))
    latest_version = s.repository.plugin_latest_version(plugin_name)
    plugin_url = s.repository.plugin_url(plugin_name, latest_version)

    data = urllib.urlopen('http://localhost:8000%s' % plugin_url).read()
    local_path = output_dir.joinpath(path(plugin_url).name)
    if not local_path.isfile():
        local_path.write_bytes(data)
        print 'Saved latest %s to %s' % (plugin_name, local_path)
    else:
        print 'File %s already exists - skipping download' % (local_path)


if __name__ == '__main__':
    args = parse_args()
    download_latest(args.plugin_name, args.output_dir)
