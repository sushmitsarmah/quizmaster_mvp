from django.contrib import admin
from .models import Quiz, Question, Answer, SelectWordQuestion

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'text', 'question_type', 'order')
    list_filter = ('quiz', 'question_type')
    search_fields = ('text',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')
    list_filter = ('question__quiz', 'is_correct')
    search_fields = ('text',)

@admin.register(SelectWordQuestion)
class SelectWordQuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'text', 'sentence')
    list_filter = ('quiz',)
    search_fields = ('text', 'sentence') 