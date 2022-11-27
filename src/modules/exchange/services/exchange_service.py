"""取引所関連のサービスモジュール"""
from abc import ABCMeta, abstractmethod

class ExchangeService(metaclass=ABCMeta):
    """取引所関連のサービスクラス"""

    @abstractmethod
    def get_latest_price(self, ticker: str, period: str) -> str:
        """指定した通貨の最新金額をドルで返します"""
        raise NotImplementedError()
