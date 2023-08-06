# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['matematika']
setup_kwargs = {
    'name': 'matematika',
    'version': '0.0.1',
    'description': 'Bu kutubxona yordamida matematik hisob kitoblarni amalga oshirish mumkin',
    'long_description': '```python\nfrom matematika import plus\nprint(plus(1,2,3,4,5)) # 15\n```',
    'author': 'Yusupov Ozodbek',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
