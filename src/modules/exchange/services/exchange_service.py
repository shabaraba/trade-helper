"""取引所関連のサービスモジュール"""
from abc import ABCMeta, abstractmethod

class ExchangeService(metaclass=ABCMeta):
    """取引所関連のサービスクラス"""

    @abstractmethod
    def get_prices(self) -> str:
        """指定した通貨の金額をドルで返します"""
        raise NotImplementedError()
