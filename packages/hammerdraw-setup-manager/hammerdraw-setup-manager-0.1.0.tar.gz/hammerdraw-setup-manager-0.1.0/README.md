# HammerDraw Setup Manager

Simple one-file module which defines defaults for the HammerDraw Core and HammerDraw plugins.

### Usage:
In your `setup.py`, add the following:

```python
# noinspection PyProtectedMember
from setuptools import _install_setup_requires
_install_setup_requires(dict(setup_requires=[ 'hammerdraw-setup-manager' ]))

from hammerdraw_setup_manager import HammerDrawSetupManager

HammerDrawSetupManager('hammerdraw.modules.my_plugin').setup \
(
    url = "https://gitlab.com/hammerdraw/my-plugin/module",
    short_description = "An example plugin for hammerdraw",
)
```

### See also:
 - [Extended Setup Tools](https://gitlab.com/Hares-Lab/tools/extended-setup-tools)
 - [HammerDraw Project](https://gitlab.com/hammerdraw)
