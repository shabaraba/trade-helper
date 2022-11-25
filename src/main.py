"""メインモジュール"""
from infrastructures import Dependency
from modules.exchange import *
from modules.notification import *

def main():
    # setup

    exchangeService = Dependency[ExchangeService]()
    print(exchangeService.__class__)

    # technicalAnalyzeService = Dependency[TechnicalAnalyzeService]()
    # notificationService = Dependency[notification_service]()

    # # get args

    # # get notification message
    # prices = exchangeService.getPrices()
    # message: str = technicalAnalyzeService.getSignal(prices)

    # # if having message, notify to slack
    message = 'test'
    if message is None : return 
    notificationService = Dependency[NotificationService]()
    print(notificationService.notify(message))


if __name__ == "__main__":
    main()