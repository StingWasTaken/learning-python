# Dependency injection with injector
from injector import Injector, inject, Module, provider, singleton

class Config:
    def __init__(self, db_url: str):
        self.db_url = db_url
        
class Database:
    def __init__(self, config: Config):
        self.config = config

    def connect(self):
        return f"Connecting to database at {self.config.db_url}"
    

class Service:
    @inject
    def __init__(self, db: Database):
        self.db = db

    def perform_action(self):
        return self.db.connect()
    
# Dependency injection with injector

class AppModule(Module):
    @singleton
    @provider
    def provide_config(self) -> Config:
        return Config("sqlite:///:memory:")
    
    @singleton
    @provider
    def provide_database(self, config: Config) -> Database:
        return Database(config)
    
    @singleton
    @provider
    def provide_service(self, db: Database) -> Service:
        return Service(db)
    
    
# Resolve dependencies using an Injector
def main():
    injector = Injector([AppModule()])
    
    # # Registering Config and Database as singletons
    # injector.binder.bind(Config, to=Config("sqlite:///:memory:"), scope=singleton)
    # injector.binder.bind(Database, to=Database, scope=singleton)
    
    # Injecting dependencies into Service
    service = injector.get(Service)
    
    # Use the service
    print(service.perform_action())
    

main()