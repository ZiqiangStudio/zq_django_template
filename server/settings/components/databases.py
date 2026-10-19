from server.settings.components.configs import DatabaseConfig

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATABASES = DatabaseConfig.get()
