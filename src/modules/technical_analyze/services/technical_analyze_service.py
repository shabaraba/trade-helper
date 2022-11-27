import abc
from ..entities.position import Position

class TechnicalAnalyzeService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def is_signal_fired(self, chart) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_expected_position(self) -> Position:
        raise NotImplementedError()

