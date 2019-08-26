from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from django.shortcuts import render
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.permissions import IsAuthenticated, AllowAny


class ArticleView(APIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (AllowAny,)

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

class ArticleCreateView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        article = request.data.get('article')
        # Create an article from the above data
        print(article)
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

class ArticleDetail(APIView):
    """
    Retrieve, update or delete a Article instance.
    """
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)