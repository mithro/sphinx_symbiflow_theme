from setuptools import setup
from sphinx_symbiflow_theme import __version__

setup(
    name = 'sphinx_symbiflow_theme',
    version = __version__,
    author = 'Based on theme by Masahiko Yasuda',
    url="https://github.com/SymbiFlow/sphinx_symbiflow_theme",
    description='Sphinx Symbiflow Theme',
    packages = ['sphinx_symbiflow_theme'],
    include_package_data=True,
    license= 'MIT License',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation"
    ],
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_symbiflow_theme = sphinx_symbiflow_theme',
        ]
    }
)

