from hammerdraw_setup_manager import CLASSIFIERS
from extended_setup import *

SingleScriptModuleSetup('hammerdraw_setup_manager').setup \
(
    short_description = "Python tool for helping making shorter and smarter setup.py scripts",
    url = 'https://gitlab.com/hammerdraw/tools/hammerdraw-setup-manager',
    min_python_version = '3.6',
    classifiers = CLASSIFIERS,
    license = 'BSD 2-clause',
)
