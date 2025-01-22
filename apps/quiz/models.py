from django.db import models
from django.conf import settings

# Create a quiz. It is a set of questions.
class Quiz(models.Model):
    class Meta:
        app_label = 'quiz'
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create a question. It is a part of a quiz.
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

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.pk:  # Only perform validation if the question is saved
            if self.question_type == self.SINGLE_ANSWER:
                if self.answer_options.filter(is_correct=True).count() != 1:
                    raise ValidationError("Single Answer questions must have exactly one correct answer.")
            
            if self.question_type == self.MULTI_ANSWER:
                if self.answer_options.filter(is_correct=True).count() < 1:
                    raise ValidationError("Multiple Answers questions must have at least one correct answer.")
            
            if self.question_type == self.SELECT_WORDS:
                if self.answer_options.filter(is_correct=True).count() < 1:
                    raise ValidationError("Select Words questions must be of type SelectWordQuestion.")

# there can be multiple answer options for a question. only one of them is correct
# for single answer questions, there is only one answer option
class AnswerOption(models.Model):
    class Meta:
        app_label = 'quiz'
    
    question = models.ForeignKey(Question, related_name='answer_options', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def clean(self):
        from django.core.exceptions import ValidationError
        
        if self.question.question_type == Question.SINGLE_ANSWER:
            if self.question.answer_options.exclude(pk=self.pk).filter(is_correct=True).exists():
                raise ValidationError("Single answer questions can only have one correct answer option.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

# Create an answer. It is a submission of an answer to a question.
class Answer(models.Model):
    class Meta:
        app_label = 'quiz'
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='answers',
        on_delete=models.CASCADE,
        null=True,  # Allow null for existing records
        blank=True  # Allow blank in forms
    )
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Add timestamp for answers

    def __str__(self):
        user_str = self.user.username if self.user else 'Anonymous'
        return f"{user_str} - {self.question.quiz.title} - Question {self.question.order}"

    def clean(self):
        from django.core.exceptions import ValidationError
        
        if self.question.question_type in [Question.MULTI_ANSWER, Question.SELECT_WORDS]:
            # For multi-answer and select words questions, check if the answer text matches one of the question's answer options
            if not self.question.answer_options.filter(text=self.text).exists():
                raise ValidationError("Submitted answer must match one of the question's answer options.")
            
            # Set is_correct based on the matched answer option
            self.is_correct = self.question.answer_options.get(text=self.text).is_correct
        else:
            # For single-answer questions, any text can be submitted as an answer
            # Set is_correct by comparing the submitted text with the correct answer's text
            correct_answer = self.question.answer_options.filter(is_correct=True).first()
            self.is_correct = (self.text == correct_answer.text)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
