from django.apps import AppConfig
from django.core.signals import setting_changed

class MembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'
    def ready(self):
        import members.signals

