from django.apps import AppConfig

class QuizConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.quiz'  # Make sure this matches our directory structure
    verbose_name = 'Quiz Application' 