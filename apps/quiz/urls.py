from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet
from .views_auth import obtain_auth_token

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
] 