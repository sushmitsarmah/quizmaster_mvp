from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .models import Quiz, Question, Answer
from .serializers import (
    QuizSerializer, 
    QuestionSerializer,
    AnswerSerializer,
    QuizAnswerSubmissionSerializer
)

class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def submit_answers(self, request, pk=None):
        quiz = self.get_object()
        serializer = QuizAnswerSubmissionSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        answers_data = serializer.validated_data['answers']
        
        try:
            with transaction.atomic():
                answers = []
                for answer_data in answers_data:
                    question_id = answer_data['question']
                    text = answer_data['text']
                    
                    try:
                        question = Question.objects.get(id=question_id, quiz=quiz)
                    except Question.DoesNotExist:
                        return Response(
                            {"error": f"Question {question_id} does not belong to this quiz"},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                    
                    answer = Answer(
                        user=request.user,
                        question=question,
                        text=text
                    )
                    answer.full_clean()  # This will run validation
                    answers.append(answer)
                
                # Save all answers
                Answer.objects.bulk_create(answers)
                
                # Calculate score
                total_questions = len(answers)
                correct_answers = sum(1 for answer in answers if answer.is_correct)
                score = (correct_answers / total_questions * 100) if total_questions > 0 else 0

                return Response({
                    'total_questions': total_questions,
                    'correct_answers': correct_answers,
                    'score': round(score, 2)
                })
                
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            ) 