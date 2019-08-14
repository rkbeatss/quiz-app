from django.urls import path
from . import views
urlpatterns = [
    path("", views.category_view, name = "main_categories"),
    path("<int:pk>/", views.quiz_view, name = "quizzes_view"),
    path("questions/<int:pk>/", views.question_view, name = "question_view"),
    ]
