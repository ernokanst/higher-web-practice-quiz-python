"""Модуль с реализацией сервиса категорий."""

from quiz.dao import AbstractCategoryService
from quiz.models import Category
from quiz.services.utils import update_instance


class CategoryService(AbstractCategoryService):
    """Реализация сервиса для категорий."""

    def list_categories(self) -> list[Category]:
        """Метод для получения списка категорий."""
        return list(Category.objects.all())

    def get_category(self, category_id: int) -> Category:
        """
        Метод для получения категории по идентификатору.

        :param category_id: Идентификатор категории.
        :return: Категория из БД.
        """
        return Category.objects.get(id=category_id)

    def create_category(self, title: str) -> Category:
        """
        Создает категорию вопросов.

        :param title: Название для категории.
        :return: Созданная категория.
        """
        category, _created = Category.objects.get_or_create(title=title)
        return category

    def update_category(self, category_id: int, data: dict) -> Category:
        """
        Обновляет категорию новыми данными.

        :param category_id: Идентификатор категории.
        :param data: Данные для обновления категории.
        :return: Обновленная категория.
        """
        category = Category.objects.get(id=category_id)
        return update_instance(category, data)

    def delete_category(self, category_id: int) -> None:
        """
        Удаляет категорию.

        :param category_id: Идентификатор категории для удаления.
        """
        category = Category.objects.get(id=category_id)
        category.delete()
