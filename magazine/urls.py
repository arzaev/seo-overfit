from django.urls import path
from .views import HomePage, ArticlePage, SubCategoryPage, TagPage
from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('article/<slug:slug>', ArticlePage.as_view(), name='article'),
    path('category/<slug:slug>', SubCategoryPage.as_view(), name='subcategory'),
    path('tag/<slug:slug>', TagPage.as_view(), name='tag')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)