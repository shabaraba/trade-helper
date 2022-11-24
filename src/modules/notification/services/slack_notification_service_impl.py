"""slack通知サービス"""
from .notification_service import NotificationService

class SlackNotificationServiceImpl(NotificationService):
    """slack通知サービス"""

    def notify(self) -> bool:
        # TODO:
        return True
