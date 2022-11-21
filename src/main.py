import injector
from dependencyBuilder import Dependency

from services import ExchangeService, NotificationService, TechnicalAnalyzeService

# setup

exchangeService = Dependency[ExchangeService]()
technicalAnalyzeService = Dependency[TechnicalAnalyzeService]()
notificationService = Dependency[NotificationService]()

# get args

# get notification message
prices = exchangeService.getPrices()
message: str = technicalAnalyzeService.getSignal(prices)

# if having message, notify to slack
if message is not None : notificationService.notify(message)
