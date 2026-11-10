from django.apps import AppConfig


class LearnConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "learn"
    verbose_name = "CodeQuest Learning Engine"

    def ready(self):
        import learn.signals  # noqa
