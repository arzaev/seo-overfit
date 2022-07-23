
from .models import ArticleCategory

general_context = {
    'description': 'сайт о фитнесе и бодибилдинге. информация о том как похудеть или накачаться. как поддерживать здооровый образ жизни.',
    'title': 'OverFitness',
    'categories': ArticleCategory.objects.all(),
}