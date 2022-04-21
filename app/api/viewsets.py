from rest_framework import serializers, viewsets
from app.api import serializers
from app import models
from rest_framework.permissions import IsAuthenticated


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.AuthorSerializer
    queryset = models.Author.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticlesSerializer
    queryset = models.Articles.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

