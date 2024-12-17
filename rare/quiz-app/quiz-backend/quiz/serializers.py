from django.contrib import admin
from django.contrib.admin import TabularInline
from rest_framework import serializers
from .models import Question, Choice, Explanation

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class ExplanationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explanation
        fields = '__all__'

