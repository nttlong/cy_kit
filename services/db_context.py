import cy_kit
class DbContext:
    def __init__(self,config=cy_kit.yaml_config("./config.yml")):
        self.config =config
        print("load config")
        print("Connec data")


    def create_default_data(self):
        print("Create default data")