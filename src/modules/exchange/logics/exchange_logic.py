"""取引所関連のビジネスロジックモジュール"""
from abc import ABC, abstractmethod

class ExchangeLogic(ABC):
    """取引所関連のビジネスロジッククラス"""

    @abstractmethod
    def get_latest_price(self, ticker: str, period: str) -> float:
        raise NotImplementedError

