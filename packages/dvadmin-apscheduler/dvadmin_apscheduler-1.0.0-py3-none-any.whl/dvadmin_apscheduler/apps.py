from django.apps import AppConfig


class DvadminApschedulerBackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dvadmin_apscheduler'
    url_prefix = "dvadmin_apscheduler"
