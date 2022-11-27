import abc

class MockTechnicalAnalyzeServiceImpl(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_signal(self, prices) -> str:
        raise NotImplementedError()

