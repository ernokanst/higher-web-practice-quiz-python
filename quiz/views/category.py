"""Модуль с контроллерами для категорий."""

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from quiz.models import Category
from quiz.serializers import CategorySerializer
from quiz.services.category import CategoryService

category_service = CategoryService()


class CategoryListCreateAPIView(APIView):
    """Эндпоинты для списка категорий и создания категории."""

    def get(self, request: Request) -> Response:
        """Возвращает список категорий."""
        categories = category_service.list_categories()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """Создаёт категорию."""
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category = category_service.create_category(serializer.validated_data['title'])
        out = CategorySerializer(category)
        return Response(out.data, status=status.HTTP_201_CREATED)


class CategoryDetailAPIView(APIView):
    """Эндпоинты для получения/обновления/удаления категории."""

    def get(self, request: Request, pk: int) -> Response:
        """Возвращает категорию по идентификатору."""
        try:
            category = category_service.get_category(pk)
        except Category.DoesNotExist:
            raise NotFound('Категория не найдена.') from None

        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        """Обновляет категорию."""
        try:
            category = category_service.get_category(pk)
        except Category.DoesNotExist:
            raise NotFound('Категория не найдена.') from None

        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated = category_service.update_category(pk, serializer.validated_data)
        out = CategorySerializer(updated)
        return Response(out.data)

    def delete(self, request: Request, pk: int) -> Response:
        """Удаляет категорию."""
        try:
            category_service.delete_category(pk)
        except Category.DoesNotExist:
            raise NotFound('Категория не найдена.') from None

        return Response(status=status.HTTP_204_NO_CONTENT)
