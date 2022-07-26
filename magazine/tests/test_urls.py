from django.test import SimpleTestCase
from django.urls import reverse, resolve
from magazine.views import HomePage, ArticlePage, SubCategoryPage, TagPage


class TestMagazineUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomePage)

    def test_article_url_is_resolved(self):
        url = reverse('article', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, ArticlePage)

    def test_sub_category_url_is_resolved(self):
        url = reverse('subcategory', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, SubCategoryPage)

    def test_tag_url_is_resolved(self):
        url = reverse('tag', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, TagPage)