# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['invitations',
 'invitations.management',
 'invitations.management.commands',
 'invitations.migrations',
 'invitations.tests']

package_data = \
{'': ['*'],
 'invitations': ['locale/de/LC_MESSAGES/*',
                 'locale/ru/LC_MESSAGES/*',
                 'locale/uk/LC_MESSAGES/*',
                 'templates/invitations/email/*',
                 'templates/invitations/forms/*',
                 'templates/invitations/messages/*']}

install_requires = \
['django>=3.2']

setup_kwargs = {
    'name': 'django-invitations',
    'version': '2.0.0',
    'description': 'Generic invitations app with support for django-allauth',
    'long_description': '# Django-invitations - Generic invitations app\n\n[![Jazzband](https://jazzband.co/static/img/badge.svg)](https://jazzband.co/)\n[![PyPI Download](https://img.shields.io/pypi/v/django-invitations.svg)](https://pypi.python.org/pypi/django-invitations)\n[![PyPI Python Versions](https://img.shields.io/pypi/pyversions/django-invitations.svg)](https://pypi.python.org/pypi/django-invitations)\n[![Build status](https://github.com/jazzband/django-invitations/actions/workflows/test.yml/badge.svg)](https://github.com/jazzband/django-invitations/actions/workflows/test.yml)\n[![Coverage status](https://codecov.io/gh/jazzband/django-invitations/branch/master/graph/badge.svg?token=xxufPt4r3I)](https://codecov.io/gh/jazzband/django-invitations)\n[![Documentation Status](https://readthedocs.org/projects/django-invitations/badge/?version=latest)](https://django-invitations.readthedocs.io/en/latest/?badge=latest)\n\n## About\n\nGeneric invitations solution with adaptable backend and support for django-allauth.\n\n## Contributing\n\nAs we are members of a [JazzBand project](https://jazzband.co/projects), `django-invitations` contributors should adhere to the [Contributor Code of Conduct](https://jazzband.co/about/conduct).\n\n### Documentation\n\nDocumentation can be found at https://django-invitations.readthedocs.io/\n',
    'author': 'bee-keeper',
    'author_email': 'None',
    'maintainer': 'JazzBand',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
