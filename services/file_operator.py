import cy_kit
import services.file_storage
from services import *
class Run:
    def __init__(self,
                 file:services.file_storage.FileStorage=cy_kit.inject(services.file_storage.FileStorage),
                 file2:services.file_storage.FileStorage=cy_kit.inject(services.file_storage.FileStorage),
                 ):
        print("init run")
        self.file=file



    def do_load_data(self):
        id= self.file.load_data("dsadadad")




class Run2:
    def __init__(self,run:Run=cy_kit.provider(Run)):
        self.data = run.file.load_data("my_code")