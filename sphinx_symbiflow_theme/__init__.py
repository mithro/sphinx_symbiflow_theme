from os import path

__version__ = '0.1.11'
__version_full__ = __version__

package_dir = path.dirname(path.abspath(__file__))

def get_path():
    return package_dir

def setup(app):
    app.add_html_theme('sphinx_symbiflow_theme', package_dir)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
