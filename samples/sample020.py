# Dependency injection with injector. Use a subclass of Config to demonstrate inheritance and dependency injection.
from injector import Injector, inject, Module, provider, singleton

class Config:
    def __init__(self, db_url: str):
        self.db_url = db_url
        
class SubConfig(Config):
    def __init__(self, db_url: str):
        super().__init__(db_url)
    

class Service:
    @inject
    def __init__(self, sub_config: SubConfig):
        self.sub_config = sub_config

    def perform_action(self):
        print(f"Performing action with database URL: {self.sub_config.db_url}")
    
# Dependency injection with injector

class AppModule(Module):
    @singleton
    @provider
    def provide_sub_config(self) -> SubConfig:
        return SubConfig("sqlite:///:memory:")

    # We don't need to provide Service here, as it will be injected automatically
    # @singleton
    # @provider
    # def provide_service(self, sub_config: SubConfig) -> Service:
    #     return Service(sub_config)
    
    
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