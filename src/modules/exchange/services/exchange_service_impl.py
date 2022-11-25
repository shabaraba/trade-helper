"""exchange_serviceクラスの継承モジュール"""
from injector import Inject
from infrastructures import Dependency

from .exchange_service import ExchangeService
from ..logics import ExchangeLogic

@Inject
class ExchangeServiceImpl(ExchangeService):
    """exchange_serviceクラスの継承クラス"""

    exchangeLogic: ExchangeLogic

    def get_latest_price(self, ticker: str, period: str) -> str:
        """指定した通貨の金額をドルで返します"""
        # TODO
        self.exchangeLogic.get_latest_price()

        # get ticker data

        # calc signal data eg. moving average

        # check signal

        # return buy or sell or settlement if signal appeared
        # and save position data to sqlite
        return 'test'
