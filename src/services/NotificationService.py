import abc

class NotificationService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def notify(self) -> bool:
        raise NotImplementedError()
