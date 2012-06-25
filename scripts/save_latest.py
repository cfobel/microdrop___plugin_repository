import sys
from path import path

project_root = path(__file__).parent.parent
sys.path.append(project_root)

from plugin_repository import PluginRepository


def parse_args():
    """Parses arguments, returns ``(options, args)``."""
    from argparse import ArgumentParser

    parser = ArgumentParser(description="""\
Download latest version of specified plugin.""",
                           )
    parser.add_argument('-s', '--server_url', dest='server_url',
            default='http://localhost:8000',
            help='Server URL (default=%(default)s')
    parser.add_argument(nargs=1, dest='plugin_name', type=str)
    parser.add_argument(nargs=1, dest='output_dir', type=path)

    args = parser.parse_args()
    args.plugin_name = args.plugin_name[0]
    args.output_dir = args.output_dir[0]
    
    return args


if __name__ == '__main__':
    args = parse_args()
    p = PluginRepository(args.server_url)
    p.download_latest(args.plugin_name, args.output_dir)
    print p.latest_version(args.plugin_name)
    print p.versions(args.plugin_name)
