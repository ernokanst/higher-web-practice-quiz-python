import pytest

from quiz.models import Category
from tests.constants import CATEGORY_TITLE_NEW, CATEGORY_TITLE_SCIENCE


@pytest.mark.django_db
class TestCategoryService:
    def test_create_and_get_category(self, category_service) -> None:
        """Тест создания и получения категории."""

        category = category_service.create_category(CATEGORY_TITLE_SCIENCE)
        fetched = category_service.get_category(category.id)
        assert fetched.title == CATEGORY_TITLE_SCIENCE

    def test_update_category(
        self,
        category_service,
        category_old: Category,
    ) -> None:
        """Тест обновления категории."""

        updated = category_service.update_category(
            category_old.id,
            {'title': CATEGORY_TITLE_NEW},
        )
        assert updated.title == CATEGORY_TITLE_NEW

    def test_delete_category(
        self,
        category_service,
        category_temp: Category,
    ) -> None:
        """Тест удаления категории."""

        category_service.delete_category(category_temp.id)
        assert Category.objects.count() == 0
