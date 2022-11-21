import abc

class ExchangeService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getPrices(self) -> str:
        raise NotImplementedError()
