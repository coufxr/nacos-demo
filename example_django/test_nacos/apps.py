from django.apps import AppConfig

from nacos_django import init_nacos


class TestNacosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_nacos'

    def ready(self):
        init_nacos()
