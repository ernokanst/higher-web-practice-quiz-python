"""Модуль с контроллерами для вопросов."""

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response

from quiz.models import Question
from quiz.serializers import QuestionSerializer
from quiz.services.question import QuestionService

question_service = QuestionService()


class QuestionViewSet(viewsets.ModelViewSet):
    """CRUD для вопросов + дополнительные эндпоинты."""

    queryset = Question.objects.select_related('quiz', 'category').all()
    serializer_class = QuestionSerializer

    @action(
        detail=False,
        methods=['get'],
        url_path=r'by_text/(?P<query>[^/.]+)',
    )
    def by_text(self, request: Request, query: str) -> Response:
        """Возвращает список вопросов по тексту."""
        questions = question_service.get_questions_by_text(query)
        serializer = self.get_serializer(questions, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='check')
    def check(self, request: Request, pk: str | None = None) -> Response:
        """Проверяет ответ на вопрос."""
        try:
            answer = request.data.get('answer', '')
            is_correct = question_service.check_answer(int(pk), str(answer))
        except (Question.DoesNotExist, ValueError):
            raise NotFound('Вопрос не найден.') from None
        return Response({'correct': is_correct}, status=status.HTTP_200_OK)
