from posixpath import join as urljoin
import logging
import httpx

logging.basicConfig()
log = logging.getLogger('resourceful')

session = httpx.Client()

GET = 'get'
PUT = 'put'
POST = 'post'
HEAD = 'head'
PATCH = 'patch'
DELETE = 'delete'
OPTIONS = 'options'

class Resource:
	def __init__(self, *args, **kwargs):
		self.parent = kwargs.get('parent')
		self.path = kwargs.get('path')
		self.url = kwargs.get('url')
		self.session = session
		self.children = []

	def request(self, method, url, **kwargs):
		rsp = self.session.request(method, url, **kwargs)
		rsp.raise_for_status()
		return rsp

	def options(self, **kwargs):
		return self.session.request(OPTIONS, self.url, **kwargs)

	def delete(self, **kwargs):
		log.debug(f"delete {self.url}")
		return self.session.request(DELETE, self.url, **kwargs)

	def post(self, **kwargs):
		log.debug(f"post {self.url}")
		return self.session.request(POST, self.url, **kwargs)

	def head(self, **kwargs):
		return self.session.request(HEAD, self.url, **kwargs)

	def patch(self, id=None, **kwargs):
		url = self.url
		if id:
			url = urljoin(self.url, id)
		log.debug(f"patch {self.url}")
		return self.session.request(PATCH, url, **kwargs)

	def put(self, id=None, **kwargs):
		url = self.url
		if id:
			url = urljoin(self.url, id)
		log.debug(f"put {self.url}")
		return self.session.request(PUT, url, **kwargs)

	def get(self, id=None, **kwargs):
		url = self.url
		if id:
			url = urljoin(self.url, id)
		log.debug(f"get {url}")
		return self.request(GET, url, **kwargs)

	def resource(self, path):
		#parts = path.rstrip('/').split('/')
		#if len(parts) > 1:
		#	return self.resource()
		#	resource = Resource(
		#		parent=self,
		#		url=urljoin(self.url, parts[0]),
		#		path=parts[0]
		#	)
		resource = Resource(
			parent=self,
			url=urljoin(self.url, path),
			path=path
		)
		setattr(self, path, resource)
		return resource

	def set_token(self, token, type='bearer'):
		self.session.headers.update(
			{
				"Authorization": f"{type.title()} {token}",
			}
		)

	def __repr__(self):
		return f"<{self.path}>"


class API(Resource):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.parent = None
