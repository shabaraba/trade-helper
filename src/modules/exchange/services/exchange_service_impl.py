"""exchange_serviceクラスの継承モジュール"""

from .exchange_service import ExchangeService

class ExchangeServiceImpl(ExchangeService):
    """exchange_serviceクラスの継承クラス"""

    def get_prices(self) -> str:
        """指定した通貨の金額をドルで返します"""
        # TODO

        # get ticker data

        # calc signal data eg. moving average

        # check signal

        # return buy or sell or settlement if signal appeared
        # and save position data to sqlite
        return 'test'
