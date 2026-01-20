"""Модуль с контроллерами для вопросов."""

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import Question
from quiz.serializers import QuestionSerializer
from quiz.services.question import QuestionService

question_service = QuestionService()


class QuestionListCreateAPIView(APIView):
    """Эндпоинты для списка вопросов и создания вопроса."""

    def get(self, request: Request) -> Response:
        """Возвращает список вопросов."""
        questions = question_service.list_questions()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """Создаёт вопрос."""
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = dict(serializer.validated_data)
        quiz = data.pop('quiz')
        question = question_service.create_question(quiz.id, data)
        out = QuestionSerializer(question)
        return Response(out.data, status=status.HTTP_201_CREATED)


class QuestionDetailAPIView(APIView):
    """Эндпоинты для получения/обновления/удаления вопроса."""

    def get(self, request: Request, pk: int) -> Response:
        """Возвращает вопрос по идентификатору."""
        try:
            question = question_service.get_question(pk)
        except Question.DoesNotExist:
            raise NotFound('Вопрос не найден.') from None
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        """Обновляет вопрос."""
        try:
            question = question_service.get_question(pk)
        except Question.DoesNotExist:
            raise NotFound('Вопрос не найден.') from None

        serializer = QuestionSerializer(question, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated = question_service.update_question(
            pk,
            serializer.validated_data,
        )
        out = QuestionSerializer(updated)
        return Response(out.data)

    def delete(self, request: Request, pk: int) -> Response:
        """Удаляет вопрос."""
        try:
            question_service.delete_question(pk)
        except Question.DoesNotExist:
            raise NotFound('Вопрос не найден.') from None
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionByTextAPIView(APIView):
    """Эндпоинт для получения списка вопросов по тексту."""

    def get(self, request: Request, query: str) -> Response:
        """Возвращает список вопросов по тексту."""
        questions = question_service.get_questions_by_text(query)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class QuestionCheckAPIView(APIView):
    """Эндпоинт для проверки ответа на вопрос."""

    def post(self, request: Request, pk: int) -> Response:
        """Проверяет ответ на вопрос."""
        try:
            answer = request.data.get('answer', '')
            is_correct = question_service.check_answer(pk, str(answer))
        except Question.DoesNotExist:
            raise NotFound('Вопрос не найден.') from None
        return Response({'correct': is_correct}, status=status.HTTP_200_OK)
