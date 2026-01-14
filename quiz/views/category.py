"""Модуль с контроллерами для категорий."""

from rest_framework import viewsets

from quiz.models import Category
from quiz.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD для категорий."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
