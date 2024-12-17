from django.urls import path
from .views import QuizView

urlpatterns = [
    path('api/quiz/', QuizView.as_view(), name='quiz-api'),  # 例: トップページのルート
]
