# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbf2csv']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['dbf2csv = dbf2csv.__main__:run'],
 'pipx.run': ['dbf2csv = dbf2csv.__main__:run']}

setup_kwargs = {
    'name': 'dbf2csv-dbase7',
    'version': '0.6.0',
    'description': 'File converter from DBF to CSV (only for dBASE 7)',
    'long_description': 'Conversión de formato DBF a CSV\n===============================\n\nScript simple para convertir ficheros de formato DBF a CSV. De momento sólo funciona para ficheros DBF "dBASE level 7".\n\nUso:\n\n```\n$ ./dbfconv.py <data.dbf>\n```',
    'author': 'chemacortes',
    'author_email': 'devxtrem@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/chemacortes/dbf2csv-py',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
