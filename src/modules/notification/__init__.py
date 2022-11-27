"""init"""
from infrastructures import Dependency
from .services.notification_service import NotificationService
from .services.slack_notification_service_impl import SlackNotificationServiceImpl


Dependency.add(NotificationService, SlackNotificationServiceImpl)


__all__ = [
    "NotificationService",
]