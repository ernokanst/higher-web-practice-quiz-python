"""Модуль с контроллерами для квизов."""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response

from quiz.models import Question, Quiz
from quiz.serializers import QuestionSerializer, QuizSerializer
from quiz.services.question import QuestionService
from quiz.services.quiz import QuizService

quiz_service = QuizService()
question_service = QuestionService()


class QuizViewSet(viewsets.ModelViewSet):
    """CRUD для квизов + дополнительные эндпоинты."""

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    @action(
        detail=False,
        methods=['get'],
        url_path=r'by_title/(?P<title>[^/.]+)',
    )
    def by_title(self, request: Request, title: str) -> Response:
        """Возвращает список квизов по названию."""
        quizzes = quiz_service.get_quizes_by_title(title)
        serializer = self.get_serializer(quizzes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='random_question')
    def random_question(
        self, request: Request, pk: str | None = None
    ) -> Response:
        """Возвращает случайный вопрос из квиза."""
        try:
            question = question_service.random_question_from_quiz(int(pk))
        except (Question.DoesNotExist, ValueError):
            raise NotFound('Квиз не найден или в нём нет вопросов.') from None
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
