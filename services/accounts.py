import cy_kit
import services.db_context

class AccountService:
    def __init__(self,db_context=cy_kit.inject(services.db_context.DbContext)):
        print("set db context for account service")
        self.db_context=db_context
        self.db_context.create_default_data()
        print("create default account")
        self.create(u=1,p=2)


    def create(self,*args,**kwargs):
        print("create account")
        print(args)
        print(kwargs)