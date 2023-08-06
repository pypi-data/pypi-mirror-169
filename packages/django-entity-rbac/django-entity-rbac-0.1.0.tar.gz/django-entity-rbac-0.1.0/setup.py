# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_entity_rbac']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'django-entity-rbac',
    'version': '0.1.0',
    'description': 'Description',
    'long_description': '# Django Entity-Relationship-based Access Control\n\ndjango-entity-rbac is an implementation of Entity-Relationship-based Access Control for Django.\n\nThis project attempts to satisfy the follow requirements:\n\n* Table-less role assignment\n* Elimination of [the role explosion problem][role-explosion]\n* Hierarchical object graphs\n* Row-level access control\n\n**django-entity-rbac is currently under heavy development.**\n\n\n## Authors\nMinkyo Seo ([@0xsaika](https://github.com/0xsaika)), Jinoh Kang ([@iamahuman](https://github.com/iamahuman))\n\n## Quick start\nCompatible with Django 3.x.\n```\npip install django-entity-rbac\n```\n\n## Usage\nSee [`roletestapp`](https://github.com/theori-io/django-entity-rbac/tree/main/roletestapp)\n\n## Documentation\nTODO\n\n[PyCon 2022 talk](https://2022.pycon.kr/program/talks/26)\n\n## Roadmap\n - [x] Release unstable API (v0.1) as proof-of-concept (kudos to Jinoh)\n - [ ] Improve API usability\n    - [ ] Redesign internal APIs\n    - [ ] Add separate permission spec classes for compose-able role declaration\n    - [ ] Replace bit fields with something less error-prone and foolproof\n - [ ] Release stable v1\n\n## License\ndjango-entity-rbac is licensed under the MIT license.\n\n[role-explosion]: https://blog.plainid.com/role-explosion-unintended-consequence-rbac\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
