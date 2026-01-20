"""Общие фикстуры для тестов."""

import pytest

from quiz.models import Category
from quiz.services.category import CategoryService
from tests.constants import CATEGORY_TITLE_OLD, CATEGORY_TITLE_TEMP


@pytest.fixture()
def category_service() -> CategoryService:
    """Возвращает сервис категорий."""
    return CategoryService()


@pytest.fixture()
def category_old() -> Category:
    """Категория для тестов обновления."""
    return Category.objects.create(title=CATEGORY_TITLE_OLD)


@pytest.fixture()
def category_temp() -> Category:
    """Категория для тестов удаления."""
    return Category.objects.create(title=CATEGORY_TITLE_TEMP)
