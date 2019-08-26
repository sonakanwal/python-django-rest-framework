from django.urls import path
from .views import AuthorView

app_name = "authors"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('authors/', AuthorView.as_view()),
    # path('create_article/', ArticleCreateView.as_view()),
    # path('articles/<int:pk>/', ArticleDetail.as_view()),
]