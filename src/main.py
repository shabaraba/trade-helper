"""メインモジュール"""
from injector import inject

from infrastructures import Dependency
from modules.exchange import *
from modules.notification import *

class Main():

    @inject
    def __init__(
        self, 
        exchangeService: ExchangeService, 
        notificationService: NotificationService
    ):
        self.exchangeService = exchangeService
        self.notificationService = notificationService

    
    def run(self):
        # setup

        print(self.exchangeService.__class__)

        # # if having message, notify to slack
        message = 'test'
        if message is None : return 
        print(self.notificationService.notify(message))


if __name__ == "__main__":
    main = Dependency[Main]
    main.run()
    