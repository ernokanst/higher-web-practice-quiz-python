"""Модуль c моделями приложения quiz"""

from django.db import models


class Category(models.Model):
    """Модель категории вопросов"""

    # TODO: Заполните поля модели


class Quiz(models.Model):
    """Модель квиза"""

    # TODO: Заполните поля модели


class Difficulty(models.TextChoices):
    """Варианты сложностей для вопросов"""

    EASY = 'easy', 'Лёгкий'
    MEDIUM = 'medium', 'Средний'
    HARD = 'hard', 'Сложный'


class Question(models.Model):
    """Модель вопроса"""

    # TODO: Заполните поля модели
