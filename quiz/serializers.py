"""Модуль c сериализаторами"""

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий"""

    # TODO: правильно реализуйте сериализатор


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для вопросов"""

    # TODO: правильно реализуйте сериализатор


class QuizSerializer(serializers.ModelSerializer):
    """Сериализатор для квизов"""

    # TODO: правильно реализуйте сериализатор
