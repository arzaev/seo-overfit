from django.views.generic import ListView, DeleteView
from .models import Article, ArticleCategory, ArticleSubCategory, Tag
from typing import Any, Dict
from .utils import general_context


class HomePage(ListView):
    """main page of portal (entry point of site)"""
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'
    paginate_by = 2
    

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(general_context)
        return context


class ArticlePage(DeleteView):
    """article Page"""
    model = Article
    template_name = 'article.html'
    slug_field = 'article_slug'


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(general_context)
        return context


class SubCategoryPage(ListView):
    """page filtered by categories"""
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'
    paginate_by = 2


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(general_context)
        return context


    def get_queryset(self) -> Article:
        slug = self.kwargs.get('slug')
        article_subcategory = ArticleSubCategory.objects.get(subcategory_slug=slug)
        articles = Article.objects.filter(article_subcategory=article_subcategory)
        return articles


class TagPage(ListView):
    """page filtered by tag"""
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'
    paginate_by = 2

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(general_context)
        return context

    def get_queryset(self) -> Article:
        slug = self.kwargs.get('slug')
        tag = Tag.objects.get(tag_slug=slug)
        articles = Article.objects.filter(article_tags=tag, is_public=True)
        return articles