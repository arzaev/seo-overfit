from django.test import TestCase, Client
from django.urls import reverse
from magazine.models import ArticleCategory, ArticleSubCategory, ArticleCategory, Tag, Article


class TestMagazineViews(TestCase):

    def setUp(self):

        test_article_category = ArticleCategory.objects.create(
            article_category='test-category'
        )

        test_article_subcategory = ArticleSubCategory.objects.create(
            article_subcategory='test-subcategory',
            subcategory_slug='test-slug-sub',
            article_category=test_article_category,
        )

        test_tag = Tag.objects.create(
            article_tag='test-tag',
            tag_slug='test-tag-slug'
        )

        test_article = Article.objects.create(
            meta_title='test-meta-title',
            article_header_image_url='test-image',
            article_description = 'test-description',
            article_title = 'test-title',
            article_content = 'test-content',
            article_subcategory = test_article_subcategory,
            article_slug = 'test-article-slug',
            is_public = True
        )

        self.client = Client()
        self.home_url = reverse('home')
        self.article_url = reverse('article', args=['test-article-slug'])
        self.subcategory_url = reverse('subcategory', args=['test-slug-sub'])
        self.tag_url = reverse('tag', args=['test-tag-slug'])

    def test_home_page_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_aritlce_page_GET(self):
        response = self.client.get(self.article_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article.html')

    def test_subcategory_page_GET(self):
        response = self.client.get(self.subcategory_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_tag_page_GET(self):
        response = self.client.get(self.tag_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
