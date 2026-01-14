"""Модуль с реализацией сервиса вопросов."""

import random

from quiz.dao import AbstractQuestionService
from quiz.models import Question, Quiz


class QuestionService(AbstractQuestionService):
    """Реализация сервиса для вопросов."""

    def list_questions(self) -> list[Question]:
        """
        Возвращает список всех вопросов.

        :return: Список вопросов.
        """
        return list(Question.objects.select_related('quiz', 'category').all())

    def get_question(self, question_id: int) -> Question:
        """
        Возвращает вопрос по его идентификатору.

        :param question_id: Идентификатор вопроса.
        :return: Вопрос из БД.
        """
        return Question.objects.select_related('quiz', 'category').get(
            id=question_id
        )

    def get_questions_by_text(self, text: str) -> list[Question]:
        """
        Возвращает вопросы по тексту.

        :param text: Текст вопроса.
        :return: Список вопросов из БД.
        """
        return list(
            Question.objects.select_related('quiz', 'category').filter(
                text__icontains=text
            )
        )

    def get_questions_for_quiz(self, quiz_id: int) -> list[Question]:
        """
        Получение вопросов по идентификатору квиза.

        :param quiz_id: Идентификатор квиза.
        :return: Список вопросов квиза.
        """
        return list(
            Question.objects.select_related('quiz', 'category').filter(
                quiz_id=quiz_id
            )
        )

    def create_question(self, quiz_id: int, data: dict) -> Question:
        """
        Создает новый вопрос.

        :param quiz_id: Идентификатор квиза, к которому относится вопрос.
        :param data: Данные из запроса для создания вопроса.
        :return: Созданный вопрос.
        """
        quiz = Quiz.objects.get(id=quiz_id)
        return Question.objects.create(quiz=quiz, **data)

    def update_question(self, question_id: int, data: dict) -> Question:
        """
        Обновляет существующий вопрос.

        :param question_id: Идентификатор вопроса.
        :param data: Данные для обновления вопроса.
        :return: Обновленный вопрос.
        """
        question = Question.objects.get(id=question_id)
        for key, value in data.items():
            setattr(question, key, value)
        question.save()
        return question

    def delete_question(self, question_id: int) -> None:
        """
        Удаляет вопрос по его идентификатору.

        :param question_id: Идентификатор вопроса для удаления.
        """
        question = Question.objects.get(id=question_id)
        question.delete()

    def check_answer(self, question_id: int, answer: str) -> bool:
        """
        Проверяет ответ на вопрос.

        :param question_id: Идентификатор вопроса.
        :param answer: Ответ пользователя.
        :return: True, если ответ правильный, False - в противном случае.
        """
        question = Question.objects.get(id=question_id)
        return question.correct_answer.strip() == answer.strip()

    def random_question_from_quiz(self, quiz_id: int) -> Question:
        """
        Возвращает случайный вопрос из указанного квиза.

        :param quiz_id: Идентификатор квиза.
        :return: Случайный вопрос из квиза.
        """
        questions = list(
            Question.objects.select_related('quiz', 'category').filter(
                quiz_id=quiz_id
            )
        )
        if not questions:
            raise Question.DoesNotExist('в этом квизе нет вопросов')
        return random.choice(questions)
