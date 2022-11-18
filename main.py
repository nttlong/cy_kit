import cy_kit
import services.accounts
import services.file_operator
import services.file_storage
import services.file_system_storage


cy_kit.config_provider(
    from_class= services.file_storage.FileStorage,
    implement_class=services.file_system_storage.FileSystemStorage
)
fx1:services.accounts.AccountService = cy_kit.inject(services.accounts.AccountService)
fx1.create(username=1,password=1)

