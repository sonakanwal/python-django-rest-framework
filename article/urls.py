from django.urls import path
from .views import ArticleView, ArticleCreateView, ArticleDetail

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('create_article/', ArticleCreateView.as_view()),
    path('articles/<int:pk>/', ArticleDetail.as_view()),
]