"""自動売買ユースケース"""
from injector import inject
from modules.exchange import ExchangeService
from modules.notification import NotificationService

class ProgramTradeUsecase:
    @inject
    def __init__(
        self, 
        exchangeService: ExchangeService, 
        notificationService: NotificationService
    ) -> None:
        self.exchangeService = exchangeService
        self.notificationService = notificationService

        self.__exec()
    
    def __exec(self):
        # setup

        print(self.exchangeService.__class__)

        # # if having message, notify to slack
        message = None
        if message is None : return 
        print(self.notificationService.notify(message))

