from django.contrib.auth.models import User
from rest_framework import serializers
from app import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


class ArticlesSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)
    author_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = models.Article
        fields = ["id", "author_id", "author", "category", "title", "summary", "first_paragraph", "body"]


class LoggedOutArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)
    author_id = serializers.UUIDField(write_only=True)
    class Meta:
        model = models.Article
        fields = ["id", "author_id", "author", "category", "title", "summary", "first_paragraph"]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'email already exists'})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'username already exists'})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)