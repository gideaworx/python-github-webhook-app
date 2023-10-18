from github_webhook_app import WebhookService

service = WebhookService()

@service.webhook
class TestService:
  def __init__(self):
    pass

service.start()