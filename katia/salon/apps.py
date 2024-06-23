from django.apps import AppConfig


class SalonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'salon'
    # Тут можно указать, например, поле verbose_name 
    # под этим именем приложение будет видно в админке.
    verbose_name = 'Страницы с описанием салона' 