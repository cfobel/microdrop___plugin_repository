# IPython log file

from path import path
import django

if __name__ == '__main__':
    project_root = path(__file__).parent.parent

    media_root = project_root.joinpath('media')
    media_root.makedirs_p()

    try:
        path(django.__file__).parent.joinpath('contrib', 'admin', 'media').link(media_root.joinpath('admin'))
    except OSError:
        path(django.__file__).parent.joinpath('contrib', 'admin', 'media').copytree(media_root.joinpath('admin'))
