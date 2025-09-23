import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestCategoryAPI:
    def test_create_and_get_category(self, client) -> None:
        """Тест создания и получения категории"""

        create_url = reverse('category-create')
        response = client.post(
            create_url,
            {'title': 'History'},
            content_type='application/json'
        )
        assert response.status_code == 201

        get_url = reverse('category-get-by-id')
        response = client.get(get_url)
        assert response.status_code == 200
        assert response.json()[0]['title'] == 'History'
