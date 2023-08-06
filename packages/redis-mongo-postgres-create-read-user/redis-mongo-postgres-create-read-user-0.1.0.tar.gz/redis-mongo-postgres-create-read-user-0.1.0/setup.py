# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['redis_mongo_postgres_read_user']

package_data = \
{'': ['*']}

install_requires = \
['psycopg2==2.9.3', 'pymongo==3.12.0', 'redis==4.3.4', 'typer==0.6.1']

entry_points = \
{'console_scripts': ['create-read-user = '
                     'redis_mongo_postgres_read_user.script:app']}

setup_kwargs = {
    'name': 'redis-mongo-postgres-create-read-user',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Script for creating read only user for MongoDB, PostgreSQL, Redis\n## PostgresQL\n- `create-read-user postgres --uri Postgres_URI -u USERNAME -p PASSWORD `\n## Redis\n- `create-read-user redis --uri Redis_URI -u USERNAME -p PASSWORD `\n## MongoDB\n- `create-read-user mongodb --uri Mongo_URI -u USERNAME -p PASSWORD `',
    'author': 'ARJUN',
    'author_email': '74967141+arjun2038@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
