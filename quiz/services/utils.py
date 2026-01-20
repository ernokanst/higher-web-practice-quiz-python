"""Вспомогательные функции для слоя сервисов."""

from __future__ import annotations

from typing import Any, TypeVar

from django.db import models

TModel = TypeVar('TModel', bound=models.Model)


def update_instance(instance: TModel, data: dict[str, Any]) -> TModel:
    """Обновляет поля модели из словаря и сохраняет объект."""
    for key, value in data.items():
        setattr(instance, key, value)
    instance.save()
    return instance
