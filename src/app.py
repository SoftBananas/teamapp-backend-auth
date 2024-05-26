from blacksheep import Application

from .core.configs import Config
from .core.database import DataBase
from .docs import docs
from .repositories.registry import RepositoryRegistry
from .services.registry import ServiceRegistry

app = Application()
docs.bind_app(app)

config = Config()
db = DataBase(config.db_config)
repositories = RepositoryRegistry(db)
services = ServiceRegistry(repositories, config)

for service in services.get_services():
    app.services.add_instance(service)
