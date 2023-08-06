# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['resourceful']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0']

setup_kwargs = {
    'name': 'resourceful',
    'version': '0.1.0',
    'description': 'Human friendly HTTP client for RESTful APIs',
    'long_description': '# resourceful\nHuman friendly HTTP client for RESTful APIs\n\n## Usage\n\n```python\n>>> import resourceful\n>>> solaire = resourceful.API(url=\'https://api.le-systeme-solaire.net/rest\')\n>>> bodies = solaire.resource(\'bodies\')\n>>> bodies.url\n\'https://api.le-systeme-solaire.net/rest/bodies\'\n>>> solaire.bodies.url\n\'https://api.le-systeme-solaire.net/rest/bodies\'\n>>> rsp = bodies.get()\n>>> rsp.json()\n{\n  "bodies": [\n    {\n      "id": "lune",\n      "name": "La Lune",\n      "englishName": "Moon",\n      "isPlanet": false,\n      "moons": null,\n      "semimajorAxis": 384400,\n      "perihelion": 363300,\n      "aphelion": 405500,\n      "eccentricity": 0.0549,\n      "inclination": 5.145,\n      "mass": {\n        "massValue": 7.346,\n        "massExponent": 22\n      },\n      "vol": {\n        "volValue": 2.1968,\n        "volExponent": 10\n      },\n      "density": 3.344,\n      "gravity": 1.62,\n      "escape": 2380,\n...\n```\n',
    'author': 'Logi Leifsson',
    'author_email': 'logileifs@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
