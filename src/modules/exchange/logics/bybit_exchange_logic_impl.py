"""取引所関連のビジネスロジックモジュール"""
from .exchange_logic import ExchangeLogic

class ByBitExchangeLogicImpl(ExchangeLogic):
    """bybitのビジネスロジッククラス"""

    def get_latest_price(self, ticker: str, period: str) -> float:
        return 0

