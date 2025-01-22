from django.db import models

class Quiz(models.Model):
    class Meta:
        app_label = 'quiz'
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    class Meta:
        app_label = 'quiz'
    
    SINGLE_ANSWER = 'single'
    MULTI_ANSWER = 'multi'
    SELECT_WORDS = 'select_words'
    
    QUESTION_TYPES = [
        (SINGLE_ANSWER, 'Single Answer'),
        (MULTI_ANSWER, 'Multiple Answers'),
        (SELECT_WORDS, 'Select Words'),
    ]

    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quiz.title} - Question {self.order}"

class Answer(models.Model):
    class Meta:
        app_label = 'quiz'
    
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class SelectWordQuestion(Question):
    class Meta:
        app_label = 'quiz'
    
    sentence = models.TextField()
    correct_words = models.JSONField(help_text='List of correct words') 