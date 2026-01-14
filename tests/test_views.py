import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
class TestCategoryAPI:
    def test_create_and_get_category(self, client: Client) -> None:
        """Тест создания и получения категории."""

        url = reverse('category-list')
        response = client.post(
            url,
            {'title': 'History'},
            content_type='application/json'
        )
        assert response.status_code == 201

        response = client.get(url)
        assert response.status_code == 200
        assert response.json()[0]['title'] == 'History'
