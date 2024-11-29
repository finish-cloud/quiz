from rest_framework import serializers
from .models import Question, Choice, Explanation

class ChoceInline(admin, TabularInline):
    model = Choice

class ExplanationInline(admin, StackedInline):
    model = Explanation

class QuestionInline(admin, ModelAdmin):
    inlines = [ChoceInline, ExplanationInline]
    list_display = ('text', 'created_at')

admin.site.register(Question, QuestionAdimn)
