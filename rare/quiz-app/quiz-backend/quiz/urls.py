from django.urls import path
from .views import QuestionListView, QuestionDetailView

urlpatterns = [
    path('api/questions/', QuestionListView.as_view(), name='question-list'),  # 例: クイズの問題ページのルート
    path('api/questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),# 例: クイズの解説詳細ページのルート
]
