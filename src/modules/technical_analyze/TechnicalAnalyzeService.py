import abc

class TechnicalAnalyzeService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getSignal(self, prices) -> str:
        raise NotImplementedError()

