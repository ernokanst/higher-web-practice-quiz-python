"""Модуль c роутингом."""

from django.urls import path

from quiz.views.category import (
    CategoryDetailAPIView,
    CategoryListCreateAPIView,
)
from quiz.views.question import (
    QuestionByTextAPIView,
    QuestionCheckAPIView,
    QuestionDetailAPIView,
    QuestionListCreateAPIView,
)
from quiz.views.quiz import (
    QuizByTitleAPIView,
    QuizDetailAPIView,
    QuizListCreateAPIView,
    QuizRandomQuestionAPIView,
)

urlpatterns = [
    path(
        'category/',
        CategoryListCreateAPIView.as_view(),
        name='category-list',
    ),
    path(
        'category/<int:pk>/',
        CategoryDetailAPIView.as_view(),
        name='category-detail',
    ),
    path('quiz/', QuizListCreateAPIView.as_view(), name='quiz-list'),
    path('quiz/<int:pk>/', QuizDetailAPIView.as_view(), name='quiz-detail'),
    path(
        'quiz/by_title/<str:title>/',
        QuizByTitleAPIView.as_view(),
        name='quiz-by-title',
    ),
    path(
        'quiz/<int:pk>/random_question/',
        QuizRandomQuestionAPIView.as_view(),
        name='quiz-random-question',
    ),
    path(
        'question/',
        QuestionListCreateAPIView.as_view(),
        name='question-list',
    ),
    path(
        'question/<int:pk>/',
        QuestionDetailAPIView.as_view(),
        name='question-detail',
    ),
    path(
        'question/by_text/<str:query>/',
        QuestionByTextAPIView.as_view(),
        name='question-by-text',
    ),
    path(
        'question/<int:pk>/check/',
        QuestionCheckAPIView.as_view(),
        name='question-check',
    ),
]
