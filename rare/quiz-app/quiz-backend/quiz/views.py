from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer


def index(request):
    return render(request, "build/index.html")

class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.prefetch_related('choice', 'explanation').all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class QuestionDetailView(APIView):
    def get(self, request, pk):
        try:
            question = Question.objects.prefetch_related('choice', 'explanation').get(pk=pk)
        except Question.DoesNotExist:
            return
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)
