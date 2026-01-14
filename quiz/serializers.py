"""Модуль c сериализаторами."""

from rest_framework import serializers

from quiz.models import Category, Question, Quiz
from quiz.validators import (normalize_non_empty_str, normalize_options,
                             validate_correct_answer_in_options,
                             validate_difficulty)


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий."""

    def validate_title(self, value: object) -> str:
        """Проверяет название категории."""
        return normalize_non_empty_str(value, 'title')

    class Meta:
        """Метаданные сериализатора Category."""

        model = Category
        fields = ['id', 'title']


class QuizSerializer(serializers.ModelSerializer):
    """Сериализатор для квизов."""

    def validate_title(self, value: object) -> str:
        """Проверяет название квиза."""
        return normalize_non_empty_str(value, 'title')

    class Meta:
        """Метаданные сериализатора Quiz."""

        model = Quiz
        fields = ['id', 'title', 'description']


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для вопросов."""

    def validate_text(self, value: object) -> str:
        """Проверяет текст вопроса."""
        return normalize_non_empty_str(value, 'text')

    def validate_difficulty(self, value: object) -> str:
        """Проверяет сложность вопроса."""
        return validate_difficulty(value)

    def validate_options(self, value: object) -> list[str]:
        """Проверяет, что варианты ответа — массив из >= 2 непустых строк."""
        return normalize_options(value)

    def validate(self, attrs: dict) -> dict:
        """Проверяет, что правильный ответ входит в варианты."""
        correct_answer = attrs.get('correct_answer')
        options = attrs.get('options')

        if correct_answer is None or options is None:
            return attrs

        normalized_options = normalize_options(options)
        validated = validate_correct_answer_in_options(
            correct_answer,
            normalized_options,
        )
        normalized_correct, normalized_options = validated
        attrs['correct_answer'] = normalized_correct
        attrs['options'] = normalized_options
        return attrs

    class Meta:
        """Метаданные сериализатора Question."""

        model = Question
        fields = [
            'id',
            'quiz',
            'category',
            'text',
            'description',
            'options',
            'correct_answer',
            'explanation',
            'difficulty',
        ]
