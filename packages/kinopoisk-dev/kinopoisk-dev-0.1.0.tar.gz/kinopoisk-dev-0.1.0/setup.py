# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kinopoisk_dev', 'kinopoisk_dev.models']

package_data = \
{'': ['*']}

install_requires = \
['grequests>=0.6.0,<0.7.0',
 'pydantic>=1.10.2,<2.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'kinopoisk-dev',
    'version': '0.1.0',
    'description': 'Реализация Api для сервиса kinopoisk.dev',
    'long_description': '<div align="center">\n    <h1>Kinopoisk Dev Api</h1>\n    <p>Python-модуль для взаимодействия с неофициальным <a href="https://kinopoisk.dev/">API КиноПоиска</a></p>\n</div>\n\n### Установка\n\n```\n$ pip install \n```\n\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/odi1n/kinopoisk_dev',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
