"""Валидаторы и нормализация данных приложения quiz."""

from rest_framework import serializers

from core.constants import DIFFICULTY_EASY, DIFFICULTY_HARD, DIFFICULTY_MEDIUM


def normalize_non_empty_str(value: object, field_name: str) -> str:
    """Проверяет строковое поле и удаляет лишние пробелы по краям."""
    if not isinstance(value, str):
        raise serializers.ValidationError(
            f'Поле "{field_name}" должно быть строкой.'
        )

    normalized = value.strip()
    if not normalized:
        raise serializers.ValidationError(
            f'Поле "{field_name}" не может быть пустым.'
        )

    return normalized


def validate_difficulty(value: object) -> str:
    """Проверяет допустимые значения сложности."""
    difficulty = normalize_non_empty_str(value, 'difficulty')
    allowed = {DIFFICULTY_EASY, DIFFICULTY_MEDIUM, DIFFICULTY_HARD}
    if difficulty not in allowed:
        raise serializers.ValidationError(
            'Поле difficulty должно быть одним из значений: easy, medium, hard.'
        )
    return difficulty


def normalize_options(value: object) -> list[str]:
    """Нормализует варианты ответа и валидирует их формат."""
    if not isinstance(value, list):
        raise serializers.ValidationError(
            'Поле options должно быть JSON-массивом (list).'
        )

    normalized: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise serializers.ValidationError(
                'Каждый вариант ответа должен быть строкой.'
            )
        option = item.strip()
        if not option:
            raise serializers.ValidationError(
                'Варианты ответа не могут быть пустыми.'
            )
        normalized.append(option)

    if len(normalized) < 2:
        raise serializers.ValidationError(
            'Должно быть минимум 2 варианта ответа.'
        )

    if len(set(normalized)) != len(normalized):
        raise serializers.ValidationError(
            'Варианты ответа не должны повторяться.'
        )

    return normalized


def validate_correct_answer_in_options(
    correct_answer: object, options: list[str]
) -> tuple[str, list[str]]:
    """Проверяет, что правильный ответ входит в варианты."""
    errors: dict[str, list[str]] = {}

    try:
        normalized_correct = normalize_non_empty_str(
            correct_answer,
            'correct_answer',
        )
    except serializers.ValidationError as exc:
        errors['correct_answer'] = exc.detail if isinstance(exc.detail, list) else [str(exc.detail)]
        raise serializers.ValidationError(errors) from None

    if normalized_correct not in options:
        errors['correct_answer'] = [
            'Правильный ответ должен быть одним из вариантов ответа.'
        ]

    if errors:
        raise serializers.ValidationError(errors)

    return normalized_correct, options
