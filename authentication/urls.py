from django.urls import path
from .views import LoginView

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
]