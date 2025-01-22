from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Quiz, Question, SelectWordQuestion
from .serializers import QuizSerializer, QuizAnswerSerializer

class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    @action(detail=True, methods=['post'])
    def submit_answers(self, request, pk=None):
        quiz = self.get_object()
        answers_data = request.data.get('answers', [])
        
        if not answers_data:
            return Response(
                {"error": "No answers provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validate all answers
        serializer = QuizAnswerSerializer(data=answers_data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        total_questions = quiz.questions.count()
        correct_answers = 0

        for answer in serializer.validated_data:
            question_id = answer['question_id']
            try:
                question = Question.objects.get(id=question_id, quiz=quiz)
            except Question.DoesNotExist:
                return Response(
                    {"error": f"Question {question_id} does not belong to this quiz"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if question.question_type == Question.SELECT_WORDS:
                select_word_question = SelectWordQuestion.objects.get(id=question_id)
                submitted_words = set(answer.get('selected_words', []))
                correct_words = set(select_word_question.correct_words)
                if submitted_words == correct_words:
                    correct_answers += 1
            else:
                submitted_answers = set(answer.get('answer_ids', []))
                correct_answers_qs = question.answers.filter(is_correct=True)
                correct_answer_ids = set(correct_answers_qs.values_list('id', flat=True))
                
                if question.question_type == Question.SINGLE_ANSWER:
                    if submitted_answers == correct_answer_ids:
                        correct_answers += 1
                elif question.question_type == Question.MULTI_ANSWER:
                    if submitted_answers == correct_answer_ids:
                        correct_answers += 1

        score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

        return Response({
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'score': round(score, 2)
        }) 