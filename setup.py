"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['mvc/ui/widgets.py']
DATA_FILES = ['mvc/widgets/osx/Resources-Widgets/MainMenu.nib']
OPTIONS = {'alias': True,
 'excludes': 'mvc.widgets.gtk',
 'packages': 'mvc',
}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
