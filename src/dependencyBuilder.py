import injector
from typing import Type, Any, Callable

from services import (
    ExchangeService,
    ExchangeServiceImpl,
    NotificationService,
    SlackNotificationServiceImpl,
    TechnicalAnalyzeService,
)


class DependencyBuilder:
    def __init__(self):
        # 依存性注入の初期化はconfigureに移譲
        self._injector = injector.Injector(self.__class__.configure)
    
    @classmethod
    def configure(cls, binder: injector.Binder) -> None:
        # ICatにEnhancedCatを紐つける
        binder.bind(ExchangeService, to=ExchangeServiceImpl)
        binder.bind(NotificationService, to=SlackNotificationServiceImpl)
        binder.bind(TechnicalAnalyzeService, to=SlackNotificationServiceImpl)
    
    def __getitem__(self, klass: Type[Any]) -> Callable:
        # 与えられたインタフェースに応じて実体クラスを返す
        return lambda: self._injector.get(klass)

Dependency = DependencyBuilder()
