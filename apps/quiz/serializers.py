from rest_framework import serializers
from .models import Quiz, Question, Answer, SelectWordQuestion

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'answers']

class SelectWordQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectWordQuestion
        fields = ['id', 'text', 'question_type', 'sentence']

class QuizSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'questions']

    def get_questions(self, obj):
        questions = obj.questions.all().order_by('order')
        serialized_questions = []
        
        for question in questions:
            if question.question_type == Question.SELECT_WORDS:
                serializer = SelectWordQuestionSerializer(question)
            else:
                serializer = QuestionSerializer(question)
            serialized_questions.append(serializer.data)
            
        return serialized_questions

class QuizAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )
    selected_words = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )

    def validate(self, data):
        question_id = data.get('question_id')
        answer_ids = data.get('answer_ids', [])
        selected_words = data.get('selected_words', [])

        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise serializers.ValidationError("Question does not exist")

        if question.question_type in [Question.SINGLE_ANSWER, Question.MULTI_ANSWER]:
            if not answer_ids:
                raise serializers.ValidationError("answer_ids is required for single/multi answer questions")
            if question.question_type == Question.SINGLE_ANSWER and len(answer_ids) > 1:
                raise serializers.ValidationError("Only one answer allowed for single answer questions")
            
            valid_answer_ids = set(question.answers.values_list('id', flat=True))
            if not all(aid in valid_answer_ids for aid in answer_ids):
                raise serializers.ValidationError("Invalid answer ID provided")

        elif question.question_type == Question.SELECT_WORDS:
            if not selected_words:
                raise serializers.ValidationError("selected_words is required for select words questions")

        return data 