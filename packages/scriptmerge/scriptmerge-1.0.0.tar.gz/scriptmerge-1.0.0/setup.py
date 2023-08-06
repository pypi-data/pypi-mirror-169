# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scriptmerge']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['scriptmerge = scriptmerge.main:main']}

setup_kwargs = {
    'name': 'scriptmerge',
    'version': '1.0.0',
    'description': 'Convert Python packages into a single script',
    'long_description': '# scriptmerge: Convert Python packages into a single script\n\nScriptmerge can be used to convert a Python script and any Python modules\nit depends on into a single-file Python script.\nThere are likely better alternatives depending on what you\'re trying to do.\nFor instance:\n\n* If you want to create a single file that can be executed by a Python interpreter,\n  use [zipapp](https://docs.python.org/3/library/zipapp.html).\n\n* If you need to create a standalone executable from your Python script,\n  I recommend using an alternative such as [PyInstaller](http://www.pyinstaller.org/).\n\nSince scriptmerge relies on correctly analysing both your script and any dependent modules,\nit may not work correctly in all circumstances.\n\n\n## Installation\n\n```sh\npip install scriptmerge\n```\n\n## Usage\n\nYou can tell scriptmerge which directories to search using the `--add-python-path` argument.\nFor instance:\n\n```sh\nscriptmerge scripts/blah --add-python-path . > /tmp/blah-standalone\n```\n\nOr to output directly to a file:\n\n```sh\nscriptmerge scripts/blah --add-python-path . --output-file /tmp/blah-standalone\n```\n\nYou can also point scriptmerge towards a Python binary that it should use\nsys.path from, for instance the Python binary inside a virtualenv:\n\n```sh\nscriptmerge scripts/blah --python-binary _virtualenv/bin/python --output-file /tmp/blah-standalone\n```\n\nSscriptmerge cannot automatically detect dynamic imports,\nbut you can use `--add-python-module` to explicitly include modules:\n\n```sh\nscriptmerge scripts/blah --add-python-module blah.util\n```\n\nScriptmerge can exclucde modules from be added to output.\nThis is useful in special cases where is it known that a module is not required to run the methods being used in the output.\nAn example might be a script that is being used as a LibreOffice macro.\nYou can use `--exclude-python-module` to explicitly exclude modules.\n\n`--exclude-python-module` takes one or more regular expressions\n\nIn this example module `blah` is excluded entirly.\n`blah\\.*` matches modules such as `blah.__init__`, `blah.my_sub_module`.\n\n```sh\nscriptmerge scripts/blah --exclude-python-module blah\\.*\n```\n\nBy default, scriptmerge will ignore the shebang in the script\nand use `"#!/usr/bin/env python"` in the output file.\nTo copy the shebang from the original script,\nuse `--copy-shebang`:\n\n```sh\nscriptmerge scripts/blah --copy-shebang --output-file /tmp/blah-standalone\n```\n\nScritpmerge can strip all doc strings and comments from imported modules using the `--clean` option.\n\n```sh\nscriptmerge --clean\n```\n\nTo see all scriptmerge options:\n\n```sh\nscriptmerge --help\n```\n\nAs you might expect with a program that munges source files, there are a\nfew caveats:\n\n* Due to the way that scriptmerge generates the output file, your script\n  source file should be encoded using UTF-8. If your script doesn\'t declare\n  its encoding in its first two lines, then it will be UTF-8 by default\n  as of Python 3.\n\n* Your script shouldn\'t have any ``from __future__`` imports.\n\n* Anything that relies on the specific location of files will probably\n  no longer work. In other words, ``__file__`` probably isn\'t all that\n  useful.\n\n* Any files that aren\'t imported won\'t be included. Static data that\n  might be part of your project, such as other text files or images,\n  won\'t be included.\n\n# Credits\n\nScriptmerge is a fork of [stickytape](https://pypi.org/project/stickytape/).\n\nCredit goes to Michael Williamson as the original author.\n',
    'author': ':Barry-Thomas-Paul: Moss',
    'author_email': 'bigbytetech@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Amourspirit/python-scriptmerge/tree/scriptmerge',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
