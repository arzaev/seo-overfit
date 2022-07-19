from cgitb import handler
from django.urls import path
from .views import index
from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)