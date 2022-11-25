"""init"""
from infrastructures import Dependency
from .exchange_logic import ExchangeLogic
from .bybit_exchange_logic_impl import ByBitExchangeLogicImpl


Dependency.add(ExchangeLogic, ByBitExchangeLogicImpl)

__all__ = [
    "ExchangeLogic",
]