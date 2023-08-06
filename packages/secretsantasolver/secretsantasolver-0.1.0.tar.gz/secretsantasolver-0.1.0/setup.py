# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['secretsantasolver']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'secretsantasolver',
    'version': '0.1.0',
    'description': '',
    'long_description': '# SecretSantaSolver\n\n## Introduction\n\nWe all know the pain of secret santas in the family. Not only will you eventually need to come up with a creative and personal gift for you loved ones, one has to first actually find a way to assign your future recipient. This often involves many rounds of discussions, scribbling down notes, drawing your own name and thus, frustration. But fear no more. With SecretSantaSolver, you can easily do these assignments in a quick and fun way!\n\n## Installation\n\nSecretSantaSolver comes with no dependencies. The recommended way to install SecretSantaSolver is via the `pip` command\n\n```\npip  install SecretSantaSolver\n```\n\nAlternatively, you can also install from the github source using poetry\n\n```\ngit clone \ncd secretsantasolver\npoetry install \n```\n\n## Usage\n\nThe main (and only) class is `SecretSantaSolver`\nYou need to pass in the names of the persons involved. \nTo enable you to also hand over the data, you can export the assigned pairs using the `export` method. This will write a `.txt` file per name to the provided path. Each file contains their secret santa, that you can send over via mail or other means.\n\n```\nimport SecretSantaSolver \n\nnames = [\n    "Alex",\n    "Jack",\n    "Jill\n]\n\nsantasolver = SecretSantaSolver.SecretSantaSolver(names = names)\nsantasolver.assign()\nsantasolver.export("path/to/folder")\n```\n\nIf you want to prevent partners being the secretsanta of each other, you can also pass in the names of their partners and set the `prohibit_partners` flag to `True`:\n\n```\nnames = [\n    "Alex",\n    "Jack",\n    "Jill\n]\n\npartners = [\n    "Jill",\n    "",\n    "Alex"\n]\n\nsantasolver = SecretSantaSolver.SecretSantaSolver(names = names, partners = partners)\nsantasolver.assign(prohibit_partners = True)\nsantasolver.export("path/to/folder")\n```',
    'author': 'Martin Helm',
    'author_email': 'martin@bio-ai.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
