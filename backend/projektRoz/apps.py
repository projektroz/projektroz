from django.apps import AppConfig


class ProjektrozConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "projektRoz"

    def ready(self):
        import projektRoz.signals