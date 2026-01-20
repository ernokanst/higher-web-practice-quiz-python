"""Конфигурация административной панели для приложения quiz."""

from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from core.constants import QUESTION_TEXT_PREVIEW_LENGTH
from quiz.models import Category, Question, Quiz


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Административная панель для модели Category."""

    list_display = ('id', 'title')
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    """Административная панель для модели Quiz."""

    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)
    ordering = ('title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Административная панель для модели Question."""

    list_display = ('id', 'text_preview', 'quiz', 'category', 'difficulty')
    list_filter = ('difficulty', 'quiz', 'category')
    search_fields = ('text', 'description')
    ordering = ('quiz', 'id')

    def get_queryset(self, request: HttpRequest) -> QuerySet[Question]:
        """Оптимизация запросов с использованием select_related."""
        return super().get_queryset(request).select_related('quiz', 'category')

    @admin.display(description='Текст вопроса')
    def text_preview(self, obj: Question) -> str:
        """Отображает текст вопроса для списка."""
        preview = obj.text[:QUESTION_TEXT_PREVIEW_LENGTH]
        if len(obj.text) > QUESTION_TEXT_PREVIEW_LENGTH:
            return preview
        return obj.text
