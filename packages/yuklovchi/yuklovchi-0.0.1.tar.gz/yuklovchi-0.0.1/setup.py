# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['yuklovchi']
install_requires = \
['instaloader>=4.9.5,<5.0.0', 'pytube>=12.1.0,<13.0.0', 'pywebio>=1.6.3,<2.0.0']

setup_kwargs = {
    'name': 'yuklovchi',
    'version': '0.0.1',
    'description': 'Bu kutobxona yordamida YouTubedan va Instagramdan yuklashingiz mumkin.',
    'long_description': '',
    'author': 'Nodir Bahodirov',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
