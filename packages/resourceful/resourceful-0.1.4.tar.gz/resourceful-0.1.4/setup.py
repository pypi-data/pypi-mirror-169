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
    'version': '0.1.4',
    'description': 'Human friendly HTTP client for RESTful APIs',
    'long_description': '# resourceful\nHuman friendly HTTP client for RESTful APIs\n\n## Usage\n\n```python\n>>> import resourceful\n>>> solaire = resourceful.API(url=\'https://api.le-systeme-solaire.net/rest\')\n>>> bodies = solaire.resource(\'bodies\')\n>>> bodies.url\n\'https://api.le-systeme-solaire.net/rest/bodies\'\n>>> solaire.bodies.url\n\'https://api.le-systeme-solaire.net/rest/bodies\'\n>>> # Perform get on https://api.le-systeme-solaire.net/rest/bodies to get all /bodies\n>>> rsp = bodies.get()\n>>> rsp.status_code\n200\n>>> rsp.json()\n{\n  "bodies": [\n    {\n      "id": "lune",\n      "name": "La Lune",\n      "englishName": "Moon",\n      "isPlanet": false,\n      "moons": null,\n      "semimajorAxis": 384400,\n      "perihelion": 363300,\n      "aphelion": 405500,\n      "eccentricity": 0.0549,\n      "inclination": 5.145,\n      "mass": {\n        "massValue": 7.346,\n        "massExponent": 22\n      },\n      "vol": {\n        "volValue": 2.1968,\n        "volExponent": 10\n      },\n      "density": 3.344,\n      "gravity": 1.62,\n      "escape": 2380,\n...\n>>> # Get resource by ID\n>>> rsp = bodies.get(\'lune\')\n>>> rsp.status_code\n200\n>>> rsp.json()\n{\'id\': \'lune\', \'name\': \'La Lune\', \'englishName\': \'Moon\', \'isPlanet\': False, \'moons\': None, \'semimajorAxis\': 384400, \'perihelion\': 363300, \'aphelion\': 405500, \'eccentricity\': 0.0549, \'inclination\': 5.145, \'mass\': {\'massValue\': 7.346, \'massExponent\': 22}, \'vol\': {\'volValue\': 2.1968, \'volExponent\': 10}, \'density\': 3.344, \'gravity\': 1.62, \'escape\': 2380.0, \'meanRadius\': 1737.0, \'equaRadius\': 1738.1, \'polarRadius\': 1736.0, \'flattening\': 0.0012, \'dimension\': \'\', \'sideralOrbit\': 27.3217, \'sideralRotation\': 655.728, \'aroundPlanet\': {\'planet\': \'terre\', \'rel\': \'https://api.le-systeme-solaire.net/rest/bodies/terre\'}, \'discoveredBy\': \'\', \'discoveryDate\': \'\', \'alternativeName\': \'\', \'axialTilt\': 6.68, \'avgTemp\': 0, \'mainAnomaly\': 0, \'argPeriapsis\': 0, \'longAscNode\': 0, \'bodyType\': \'Moon\'}\n>>> # Perform get on https://api.le-systeme-solaire.net/rest/bodies with query parameters\n>>> rsp = bodies.get(params={\'data\': \'id,name,isPlanet\', \'filter[]\': \'isPlanet,eq,true\'})\n>>> rsp.status_code\n200\n>>> rsp.json()\n{\'bodies\': [{\'id\': \'uranus\', \'name\': \'Uranus\', \'isPlanet\': True}, {\'id\': \'neptune\', \'name\': \'Neptune\', \'isPlanet\': True}, {\'id\': \'jupiter\', \'name\': \'Jupiter\', \'isPlanet\': True}, {\'id\': \'mars\', \'name\': \'Mars\', \'isPlanet\': True}, {\'id\': \'mercure\', \'name\': \'Mercure\', \'isPlanet\': True}, {\'id\': \'saturne\', \'name\': \'Saturne\', \'isPlanet\': True}, {\'id\': \'terre\', \'name\': \'La Terre\', \'isPlanet\': True}, {\'id\': \'venus\', \'name\': \'Vénus\', \'isPlanet\': True}]}\n```\n',
    'author': 'Logi Leifsson',
    'author_email': 'logileifs@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/logileifs/resourceful',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
