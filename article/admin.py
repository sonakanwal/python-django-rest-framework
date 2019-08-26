from django.contrib import admin
from .models import Author, Article

# Register your models
admin.site.register(Article)
admin.site.register(Author)
