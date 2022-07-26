from rest_framework import generics
from .models import ArticleCategory, ArticleSubCategory, Article, Tag
from .serializers import MainSerializer


class MainAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = MainSerializer