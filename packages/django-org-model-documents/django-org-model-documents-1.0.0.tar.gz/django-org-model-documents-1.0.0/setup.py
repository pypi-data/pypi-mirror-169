# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['org_model_documents', 'org_model_documents.migrations']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'django-org-model-documents',
    'version': '1.0.0',
    'description': 'A Django app to allow attaching any number of documents to any model in a project.',
    'long_description': None,
    'author': 'Oak McIlwain',
    'author_email': 'oak.mcilwain@dbca.wa.gov.au',
    'maintainer': 'DBCA OIM',
    'maintainer_email': 'asi@dbca.wa.gov.au',
    'url': None,
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
