"""Модуль с контроллерами для квизов."""

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import Question, Quiz
from quiz.serializers import QuestionSerializer, QuizSerializer
from quiz.services.question import QuestionService
from quiz.services.quiz import QuizService

quiz_service = QuizService()
question_service = QuestionService()


class QuizListCreateAPIView(APIView):
    """Эндпоинты для списка квизов и создания квиза."""

    def get(self, request: Request) -> Response:
        """Возвращает список квизов."""
        quizzes = quiz_service.list_quizzes()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """Создаёт квиз."""
        serializer = QuizSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quiz = quiz_service.create_quiz(serializer.validated_data)
        out = QuizSerializer(quiz)
        return Response(out.data, status=status.HTTP_201_CREATED)


class QuizDetailAPIView(APIView):
    """Эндпоинты для получения/обновления/удаления квиза."""

    def get(self, request: Request, pk: int) -> Response:
        """Возвращает квиз по идентификатору."""
        try:
            quiz = quiz_service.get_quiz(pk)
        except Quiz.DoesNotExist:
            raise NotFound('Квиз не найден.') from None
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        """Обновляет квиз."""
        try:
            quiz = quiz_service.get_quiz(pk)
        except Quiz.DoesNotExist:
            raise NotFound('Квиз не найден.') from None

        serializer = QuizSerializer(quiz, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated = quiz_service.update_quiz(pk, serializer.validated_data)
        out = QuizSerializer(updated)
        return Response(out.data)

    def delete(self, request: Request, pk: int) -> Response:
        """Удаляет квиз."""
        try:
            quiz_service.delete_quiz(pk)
        except Quiz.DoesNotExist:
            raise NotFound('Квиз не найден.') from None
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuizByTitleAPIView(APIView):
    """Эндпоинты для получения списка квизов по названию."""

    def get(self, request: Request, title: str) -> Response:
        """Возвращает список квизов по названию."""
        quizzes = quiz_service.get_quizes_by_title(title)
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)


class QuizRandomQuestionAPIView(APIView):
    """Эндпоинты для получения случайного вопроса из квиза."""

    def get(self, request: Request, pk: int) -> Response:
        """Возвращает случайный вопрос из квиза."""
        try:
            question = question_service.random_question_from_quiz(pk)
        except Question.DoesNotExist:
            raise NotFound('Квиз не найден или в нём нет вопросов.') from None

        serializer = QuestionSerializer(question)
        return Response(serializer.data)
