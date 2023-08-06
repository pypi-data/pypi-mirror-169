import os
from collections import namedtuple
from itertools import accumulate

try:
    import extended_setup
except ImportError:
    from setuptools import _install_setup_requires
    _install_setup_requires(dict(setup_requires=[ 'extended-setup-tools' ]))

from extended_setup import cached_property, _MISSING
from extended_setup import ExtendedSetupManager
from typing import *
from typing.io import *

CLASSIFIERS = \
[
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]

class HammerDrawSetupManager(ExtendedSetupManager):
    def __init__(self, root_module_name: str, *args, init_script_filename: str = '__init__.py', **kwargs):
        super().__init__(root_module_name=root_module_name, *args, **kwargs)
        self.init_script_filename = init_script_filename
    
    @cached_property
    def init_script_file(self) -> TextIO:
        return open(os.path.join(self.sources_dir, self.root_module_name, self.init_script_filename), 'rt')
    
    @cached_property
    def classifiers(self) -> List[str]:
        return CLASSIFIERS
    
    @cached_property
    def url_prefix(self):
        return '''https://gitlab.com/hammerdraw/'''
    
    def make_setup_kwargs(self, **kwargs) -> Dict[str, Any]:
        defaults = dict \
        (
            license = "BSD 2-clause",
            min_python_version = kwargs.pop('min_python_version') or '3.6.0',
            keywords = [ 'image', 'tabletop', 'hammerdraw' ],
            include_package_data = True,
        )
        
        defaults.update(kwargs)
        kwargs = defaults
        
        namespace_packages = { 'hammerdraw', 'hammerdraw.modules' }
        pkgs = kwargs.pop('namespace_packages', _MISSING)
        if (pkgs is _MISSING):
            namespace_packages.update(accumulate(self.root_module_name.split('.')[:-1], cast(Callable[[str, str], str], '{}.{}'.format)))
        else:
            namespace_packages.update(pkgs)
        namespace_packages = list(sorted(namespace_packages))
        
        classifiers = kwargs.pop('classifiers', _MISSING)
        if (classifiers is _MISSING):
            classifiers = self.classifiers
        
        return super(HammerDrawSetupManager, self).make_setup_kwargs(namespace_packages=namespace_packages, classifiers=classifiers, **kwargs)
    
    @overload
    def setup(self, *, short_description: str, url: str = _MISSING, **kwargs):
        pass
    def setup(self, *, classifiers=_MISSING, **kwargs):
        return super(HammerDrawSetupManager, self).setup(classifiers=classifiers, **kwargs)



__title__ = 'hammerdraw-setup-manager'
__author__ = 'Peter Zaitcev / USSX Hares'
__license__ = 'BSD 2-clause'
__copyright__ = 'Copyright 2021 Peter Zaitcev'
__version__ = '0.1.0'

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
version_info = VersionInfo(*__version__.split('.'), releaselevel='alpha', serial=0)


__all__ = \
[
    'version_info',
    '__title__',
    '__author__',
    '__license__',
    '__copyright__',
    '__version__',
    
    'CLASSIFIERS',
    'HammerDrawSetupManager',
]
