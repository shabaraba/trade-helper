"""slack通知サービス"""
import slackweb
from infrastructures import SLACK_WEBHOOK_URL

from .notification_service import NotificationService

class SlackNotificationServiceImpl(NotificationService):
    """slack通知サービス"""

    def notify(self, message: str) -> bool:
        # TODO:
        slack = slackweb.Slack(url=SLACK_WEBHOOK_URL)
        slack.notify(text="Pythonからslackへ通知する")
        return True
