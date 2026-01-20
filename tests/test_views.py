from http import HTTPStatus

import pytest
from django.test import Client
from django.urls import reverse

from tests.constants import CATEGORY_TITLE_HISTORY


@pytest.mark.django_db
class TestCategoryAPI:
    def test_create_and_get_category(self, client: Client) -> None:
        """Тест создания и получения категории."""

        url = reverse('category-list')
        response = client.post(
            url,
            {'title': CATEGORY_TITLE_HISTORY},
            content_type='application/json',
        )
        assert response.status_code == HTTPStatus.CREATED

        response = client.get(url)
        assert response.status_code == HTTPStatus.OK
        assert response.json()[0]['title'] == CATEGORY_TITLE_HISTORY
