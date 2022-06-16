"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.api import viewsets
from app.api.viewsets import Register, LoggedOutArticleSerializer, AuthorDocumentView, ArticleDocumentView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings
route = routers.DefaultRouter()

route.register(r'admin/authors', viewsets.AuthorViewSet, basename="author")
route.register(r'admin/articles', viewsets.ArticleViewSet, basename='article')
route.register(r'articles', viewsets.AnonymousArticleViewSet, basename='Articles')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/login/refresh', TokenRefreshView.as_view()),
    path('api/sign-up/', Register.as_view(), name='register'),
    path('author/search/', AuthorDocumentView.as_view({'get': 'list'}), name='author'),
    path('articles/search/', ArticleDocumentView.as_view({'get': 'list'}), name='articleview'),

    path('api/', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



