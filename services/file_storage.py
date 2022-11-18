class FileStorage:
    def load_config(self):
        print("FileStorage load config")

    @classmethod
    def load_data(cls,path:str):
        print(f"FileStorage load_data {path}")