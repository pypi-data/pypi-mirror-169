# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['impersonation']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'impersonation',
    'version': '0.1.1',
    'description': 'Utility for user impersonation by running instructions under given user',
    'long_description': '*************\nimpersonation\n*************\n\n.. image:: https://img.shields.io/pypi/v/impersonation\n    :target: https://pypi.org/project/impersonation\n    :alt: PyPI version\n.. image:: https://github.com/rena2damas/impersonation/actions/workflows/ci.yaml/badge.svg\n    :target: https://github.com/rena2damas/impersonation/actions/workflows/ci.yaml\n    :alt: CI\n.. image:: https://codecov.io/gh/rena2damas/impersonation/branch/master/graph/badge.svg\n    :target: https://app.codecov.io/gh/rena2damas/impersonation/branch/master\n    :alt: codecov\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n    :alt: code style: black\n.. image:: https://img.shields.io/badge/License-MIT-yellow.svg\n    :target: https://opensource.org/licenses/MIT\n    :alt: license: MIT\n\nA utility that allows a certain routine to run under a given user. To achieve this, a\nprocess will run under the ``uid`` and ``gid`` of the intended user. For that\nreason, it is a requirement that the running process has ``SETUID`` and\n``SETGID`` capabilities.\n\nFeatures\n========\n* decorator for instance methods\n* decorator for ``classmethod`` and ``staticmethod``\n* decorator for classes\n\nInstallation\n============\nInstall the package directly from ``PyPI`` (recommended):\n\n.. code-block:: bash\n\n    $ pip install -U impersonation\n\nExample usage\n=============\nA simple example on how to work with a ``Flask`` application:\n\n.. code-block:: python\n\n    from impersonation import impersonate\n\n    # it works on functions\n    @impersonate("other")\n    def printer(string):\n        print(string)\n\n\n    # ... and classes\n    @impersonate("other")\n    class Printer:\n        def __init__(self, prefix=""):\n            self.prefix = prefix\n\n        def printer1(self, string):\n            print(f"{self.prefix}{string}")\n\n        @staticmethod\n        def printer2(string):\n            print(string)\n\nTests & linting 🚥\n==================\nRun tests with ``tox``:\n\n.. code-block:: bash\n\n    # ensure tox is installed\n    $ tox\n\nRun linter only:\n\n.. code-block:: bash\n\n    $ tox -e lint\n\nOptionally, run coverage as well with:\n\n.. code-block:: bash\n\n    $ tox -e coverage\n\nLicense\n=======\nMIT licensed. See `LICENSE <LICENSE>`__.\n',
    'author': 'Renato Damas',
    'author_email': 'rena2damas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rena2damas/impersonation',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
