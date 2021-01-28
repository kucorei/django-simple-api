# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_simple_api']

package_data = \
{'': ['*'], 'django_simple_api': ['templates/*']}

install_requires = \
['django', 'pydantic>=1.7.3,<2.0.0']

setup_kwargs = {
    'name': 'django-simple-api',
    'version': '0.1.0',
    'description': 'A non-intrusive component that can help you quickly create APIs.',
    'long_description': '# Django Simple API\n\nA non-intrusive component that can help you quickly create APIs.\n\n## Install\n\nDownload and install from github\n\n```\npip install git+https://github.com/abersheeran/django-simple-api.git@setup.py\n```\n\nAdd django-simple-api to your `INSTALLED_APPS` in settings:\n\n```python\nINSTALLED_APPS = [\n    ...\n    "django_simple_api",\n]\n```\n\nAdd `SimpleApiMiddleware` to your `MIDDLEWARE` in settings:\n\n```python\nMIDDLEWARE = [\n    ...\n    "django_simple_api.middleware.SimpleApiMiddleware",\n]\n```\n\n## Usage\n',
    'author': 'abersheeran',
    'author_email': 'me@abersheeran.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abersheeran/django-simple-api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

