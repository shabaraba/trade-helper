"""取引所関連のサービスモジュール"""
from abc import ABC, abstractmethod

class ExchangeService(ABC):
    """取引所関連のサービスクラス"""

    @abstractmethod
    def get_prices(self) -> str:
        """指定した通貨の金額をドルで返します"""
        raise NotImplementedError()
