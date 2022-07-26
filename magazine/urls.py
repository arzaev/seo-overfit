from django.urls import path
from .views import HomePage, ArticlePage, SubCategoryPage, TagPage
from config import settings
from django.conf.urls.static import static
from .views_api import MainAPIView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('article/<slug:slug>', ArticlePage.as_view(), name='article'),
    path('category/<slug:slug>', SubCategoryPage.as_view(), name='subcategory'),
    path('tag/<slug:slug>', TagPage.as_view(), name='tag'),

    path('api/v1/articlelist/', MainAPIView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)