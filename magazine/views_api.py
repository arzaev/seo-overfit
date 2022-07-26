from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import ArticleCategory, ArticleSubCategory, Article, Tag
from .serializers import MainSerializer


class MainAPIView(APIView):
    def get(self, request):
        lst = Article.objects.all().values()
        return Response({'articles': lst})

    def post(self, request):
        return Response({'post': 'yeah'})


# class MainAPIView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = MainSerializer