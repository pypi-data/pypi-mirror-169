# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['recon', 'recon.cli', 'recon.operations', 'recon.prodigy']

package_data = \
{'': ['*'], 'recon.prodigy': ['templates/*']}

install_requires = \
['click-completion',
 'colorama',
 'numpy>=1.20.0',
 'pydantic>=1.9,<2.0',
 'scipy>=1.7.0,<1.9',
 'spacy>=3.2.0,<3.5.0',
 'xxhash>=3.0.0,<4.0']

entry_points = \
{'console_scripts': ['recon = recon.cli:app'],
 'prodigy_recipes': ['recon.ner_correct = recon:prodigy_recipes.ner_correct',
                     'recon.ner_merge = recon:prodigy_recipes.ner_merge']}

setup_kwargs = {
    'name': 'reconner',
    'version': '0.10.0',
    'description': 'Recon NER, Debug and correct annotated Named Entity Recognition (NER) data for inconsitencies and get insights on improving the quality of your data.',
    'long_description': 'None',
    'author': 'Kabir Khan',
    'author_email': 'kabirkhan1137@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://kabirkhan.github.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
