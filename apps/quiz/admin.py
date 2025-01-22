from django.contrib import admin
from django import forms
from .models import Quiz, Question, AnswerOption, Answer

class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    extra = 1
    min_num = 1  # Require at least one answer option
    validate_min = True

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    show_change_link = True

class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'answer_options' in self.fields and not self.instance.pk:
            # If the question is not saved yet, disable the answer options field
            self.fields['answer_options'].widget.attrs['disabled'] = True

    def clean(self):
        # Perform any additional form-level validation if needed
        pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'text', 'question_type', 'order')
    list_filter = ('quiz', 'question_type')
    search_fields = ('text',)
    inlines = [AnswerOptionInline]
    form = QuestionAdminForm
    
    def get_changeform_initial_data(self, request):
        # Set default order value when creating a new question
        return {'order': Question.objects.count() + 1}

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'text', 'is_correct', 'created_at')
    list_filter = ('question__quiz', 'is_correct', 'user')
    search_fields = ('text', 'user__username')
    readonly_fields = ('is_correct', 'created_at') 