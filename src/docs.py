from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

docs = OpenAPIHandler(info=Info(title="TEAMAPP Auth", version="0.0.1"))
