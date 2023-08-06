# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pureml',
 'pureml.cli',
 'pureml.config',
 'pureml.integrations',
 'pureml.integrations.mlflow',
 'pureml.integrations.mlflow.deployer',
 'pureml.models',
 'pureml.models.model_packaging']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.4.0,<3.0.0',
 'PyYAML>=6.0,<7.0',
 'numpy>=1.23.1,<2.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'requests>=2.28.1,<3.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['pure = pureml.cli.main:app']}

setup_kwargs = {
    'name': 'pureml',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Pure\n',
    'author': 'vamsidhar muthireddy',
    'author_email': 'vamsi.muthireddy@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
