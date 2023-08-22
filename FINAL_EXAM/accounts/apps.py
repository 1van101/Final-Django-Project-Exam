from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FINAL_EXAM.accounts'

    def ready(self):
        result = super().ready()
        import FINAL_EXAM.accounts.signals

        return result
