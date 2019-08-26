from rest_framework import serializers
from article.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120)
    email = serializers.EmailField()

    class Meta:
        model = Author
        fields = ('id','name', 'email')
