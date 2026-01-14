"""Модуль c моделями приложения quiz."""

from django.db import models

from core.constants import (CATEGORY_TITLE_MAX_LENGTH, DIFFICULTY_CHOICES,
                            DIFFICULTY_EASY, DIFFICULTY_MAX_LENGTH,
                            QUESTION_CORRECT_ANSWER_MAX_LENGTH,
                            QUESTION_DESCRIPTION_MAX_LENGTH,
                            QUESTION_EXPLANATION_MAX_LENGTH,
                            QUESTION_TEXT_MAX_LENGTH,
                            QUIZ_DESCRIPTION_MAX_LENGTH, QUIZ_TITLE_MAX_LENGTH)


class Category(models.Model):
    """Модель категории вопросов."""

    title = models.CharField(
        max_length=CATEGORY_TITLE_MAX_LENGTH,
        unique=True,
        verbose_name='Название',
    )

    def __str__(self) -> str:
        """Строковое представление категории."""
        return self.title

    class Meta:
        """Метаданные модели Category."""

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Quiz(models.Model):
    """Модель квиза."""

    title = models.CharField(
        max_length=QUIZ_TITLE_MAX_LENGTH,
        verbose_name='Название',
    )
    description = models.TextField(
        max_length=QUIZ_DESCRIPTION_MAX_LENGTH,
        blank=True,
        default='',
        verbose_name='Описание',
    )

    def __str__(self) -> str:
        """Строковое представление квиза."""
        return self.title

    class Meta:
        """Метаданные модели Quiz."""

        verbose_name = 'Квиз'
        verbose_name_plural = 'Квизы'


class Question(models.Model):
    """Модель вопроса."""

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Квиз',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Категория',
    )
    text = models.CharField(
        max_length=QUESTION_TEXT_MAX_LENGTH,
        verbose_name='Текст вопроса',
    )
    description = models.TextField(
        max_length=QUESTION_DESCRIPTION_MAX_LENGTH,
        blank=True,
        default='',
        verbose_name='Описание',
    )
    options = models.JSONField(verbose_name='Варианты ответа')
    correct_answer = models.CharField(
        max_length=QUESTION_CORRECT_ANSWER_MAX_LENGTH,
        verbose_name='Правильный ответ',
    )
    explanation = models.TextField(
        max_length=QUESTION_EXPLANATION_MAX_LENGTH,
        blank=True,
        default='',
        verbose_name='Пояснение',
    )
    difficulty = models.CharField(
        max_length=DIFFICULTY_MAX_LENGTH,
        choices=DIFFICULTY_CHOICES,
        default=DIFFICULTY_EASY,
        verbose_name='Сложность',
    )

    def __str__(self) -> str:
        """Строковое представление вопроса."""
        return self.text

    class Meta:
        """Метаданные модели Question."""

        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
