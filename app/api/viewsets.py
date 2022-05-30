import uuid
from rest_framework import filters, generics, status
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from app.api import serializers
from app import models
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
import django_filters
from app.api.serializers import LoggedOutArticleSerializer, ArticlesSerializer, RegisterSerializer
from app.models import Article


class AuthorViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'id']


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    serializer_class = serializers.ArticlesSerializer
    queryset = models.Article.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'author__name', 'title', 'body']

    # def get_serializer_class(self):
    #     if self.request.user.is_authenticated:
    #         return ArticlesSerializer
    #     else:
    #         return LoggedOutArticleSerializer


class AnonymousArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.LoggedOutArticleSerializer
    queryset = models.Article.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'author__name', 'title', 'body']

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return ArticlesSerializer
        else:
            return LoggedOutArticleSerializer


class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",

                "User": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)