"""自動売買ユースケース"""
from injector import inject
from modules.exchange import ExchangeService
from modules.notification import NotificationService
from modules.technical_analyze import TechnicalAnalyzeService

class ProgramTradeUsecase:
    @inject
    def __init__(
        self, 
        exchangeService: ExchangeService, 
        notificationService: NotificationService,
        technicalAnalyzeService: TechnicalAnalyzeService
    ) -> None:
        self.exchange = exchangeService
        self.notification = notificationService
        self.ta = technicalAnalyzeService

        self.__exec()
    
    def __exec(self):
        ticker: str = 'btc/usdt'
        period: str = '15'
        term: int = 400
        
        # 取引所から指定期間内の価格を取得する
        chart: list[float] = self.exchange.fetch_chart(ticker, period, term)
        # 取得した価格でシグナルが出ているか判定する
        if not self.ta.is_signal_fired(chart): return

        # シグナルが出ているならメッセージを作成する
        message: str = str(self.ta.get_expected_position())
        # 通知する
        self.notification.notify(message)
        # FIXME 各サービスのentityで受け取っているので、dtoに変換してusecaseに渡すこと
        # FIXME dxoクラスを作成すること
