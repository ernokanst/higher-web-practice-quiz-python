import pytest
from quiz.models import Category
from quiz.services.category import CategoryService


@pytest.mark.django_db
class TestCategoryService:
    def setup_method(self) -> None:
        """Подготавливает сервис"""

        self.service = CategoryService()

    def test_create_and_get_category(self) -> None:
        """Тест создания и получения категории"""

        category = self.service.create_category('Science')
        fetched = self.service.get_category(category.id)
        assert fetched.title == 'Science'

    def test_update_category(self) -> None:
        """Тест обновления категории"""

        category = Category.objects.create(name='Old')
        updated = self.service.update_category(category.id, {'title': 'New'})
        assert updated.title == 'New'

    def test_delete_category(self) -> None:
        """Тест удаления категории"""

        category = Category.objects.create(name='Temp')
        self.service.delete_category(category.id)
        assert Category.objects.count() == 0
