from rest_framework import serializers
from .models import Article


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('article_title', 'id')