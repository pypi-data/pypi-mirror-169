from posixpath import join as urljoin
import logging
import asyncio
import httpx

logging.basicConfig()
log = logging.getLogger('resourceful')

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
		self.session = httpx.Client()
		self.asession = httpx.AsyncClient()
		self.children = []
		self.loop = asyncio.get_event_loop()

	def request(self, method, url, sync=True, **kwargs):
		if not sync:
			return asyncio.ensure_future(
				self.asession.request(method, url, **kwargs)
			)
		else:
			rsp = self.session.request(method, url, **kwargs)
		rsp.raise_for_status()
		return rsp

	def arequest(self, method, url, **kwargs):
		return self.request(method, url, sync=False, **kwargs)

	def options(self, sync=True, **kwargs):
		return self.session.request(OPTIONS, self.url, sync=sync, **kwargs)

	def aoptions(self, **kwargs):
		return self.options(sync=False, **kwargs)

	def delete(self, sync=True, **kwargs):
		log.debug(f"delete {self.url}")
		return self.session.request(DELETE, self.url, sync=sync, **kwargs)

	def adelete(self, **kwargs):
		return self.delete(sync=False, **kwargs)

	def post(self, sync=True, **kwargs):
		log.debug(f"post {self.url}")
		return self.session.request(POST, self.url, sync=sync, **kwargs)

	def apost(self, **kwargs):
		return self.post(sync=False, **kwargs)

	def head(self, sync=True, **kwargs):
		return self.session.request(HEAD, self.url, sync=sync, **kwargs)

	def ahead(self, **kwargs):
		return self.head(sync=False, **kwargs)

	def patch(self, id=None, sync=True, **kwargs):
		url = self.url
		if id:
			url = urljoin(self.url, id)
		log.debug(f"patch {self.url}")
		return self.session.request(PATCH, url, sync=sync **kwargs)

	def apatch(self, id=None, **kwargs):
		return self.patch(id=id, sync=False, **kwargs)

	def put(self, id=None, sync=True, **kwargs):
		url = self.url
		if id:
			url = urljoin(self.url, id)
		log.debug(f"put {self.url}")
		return self.session.request(PUT, url, sync=sync, **kwargs)

	def aput(self, id=None, **kwargs):
		return self.put(id=id, sync=False, **kwargs)

	def get(self, id=None, sync=True, **kwargs):
		url = self.url
		if id:
			url = urljoin(self.url, id)
		log.debug(f"get {url}")
		return self.request(GET, url, sync=sync, **kwargs)

	def aget(self, id=None, **kwargs):
		return self.get(id=id, sync=False, **kwargs)

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
