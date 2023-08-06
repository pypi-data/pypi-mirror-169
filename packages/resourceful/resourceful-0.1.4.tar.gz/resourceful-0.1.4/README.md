# resourceful
Human friendly HTTP client for RESTful APIs

## Usage

```python
>>> import resourceful
>>> solaire = resourceful.API(url='https://api.le-systeme-solaire.net/rest')
>>> bodies = solaire.resource('bodies')
>>> bodies.url
'https://api.le-systeme-solaire.net/rest/bodies'
>>> solaire.bodies.url
'https://api.le-systeme-solaire.net/rest/bodies'
>>> # Perform get on https://api.le-systeme-solaire.net/rest/bodies to get all /bodies
>>> rsp = bodies.get()
>>> rsp.status_code
200
>>> rsp.json()
{
  "bodies": [
    {
      "id": "lune",
      "name": "La Lune",
      "englishName": "Moon",
      "isPlanet": false,
      "moons": null,
      "semimajorAxis": 384400,
      "perihelion": 363300,
      "aphelion": 405500,
      "eccentricity": 0.0549,
      "inclination": 5.145,
      "mass": {
        "massValue": 7.346,
        "massExponent": 22
      },
      "vol": {
        "volValue": 2.1968,
        "volExponent": 10
      },
      "density": 3.344,
      "gravity": 1.62,
      "escape": 2380,
...
>>> # Get resource by ID
>>> rsp = bodies.get('lune')
>>> rsp.status_code
200
>>> rsp.json()
{'id': 'lune', 'name': 'La Lune', 'englishName': 'Moon', 'isPlanet': False, 'moons': None, 'semimajorAxis': 384400, 'perihelion': 363300, 'aphelion': 405500, 'eccentricity': 0.0549, 'inclination': 5.145, 'mass': {'massValue': 7.346, 'massExponent': 22}, 'vol': {'volValue': 2.1968, 'volExponent': 10}, 'density': 3.344, 'gravity': 1.62, 'escape': 2380.0, 'meanRadius': 1737.0, 'equaRadius': 1738.1, 'polarRadius': 1736.0, 'flattening': 0.0012, 'dimension': '', 'sideralOrbit': 27.3217, 'sideralRotation': 655.728, 'aroundPlanet': {'planet': 'terre', 'rel': 'https://api.le-systeme-solaire.net/rest/bodies/terre'}, 'discoveredBy': '', 'discoveryDate': '', 'alternativeName': '', 'axialTilt': 6.68, 'avgTemp': 0, 'mainAnomaly': 0, 'argPeriapsis': 0, 'longAscNode': 0, 'bodyType': 'Moon'}
>>> # Perform get on https://api.le-systeme-solaire.net/rest/bodies with query parameters
>>> rsp = bodies.get(params={'data': 'id,name,isPlanet', 'filter[]': 'isPlanet,eq,true'})
>>> rsp.status_code
200
>>> rsp.json()
{'bodies': [{'id': 'uranus', 'name': 'Uranus', 'isPlanet': True}, {'id': 'neptune', 'name': 'Neptune', 'isPlanet': True}, {'id': 'jupiter', 'name': 'Jupiter', 'isPlanet': True}, {'id': 'mars', 'name': 'Mars', 'isPlanet': True}, {'id': 'mercure', 'name': 'Mercure', 'isPlanet': True}, {'id': 'saturne', 'name': 'Saturne', 'isPlanet': True}, {'id': 'terre', 'name': 'La Terre', 'isPlanet': True}, {'id': 'venus', 'name': 'Vénus', 'isPlanet': True}]}
```
