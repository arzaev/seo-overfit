from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    article_category = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.article_category


class ArticleSubCategory(models.Model):
    article_subcategory = models.CharField(max_length=255, unique=True)
    subcategory_slug = models.SlugField(max_length=255, unique=True)
    article_category = models.ForeignKey(ArticleCategory,
                                         verbose_name="Category",
                                         on_delete=models.CASCADE
                                         )

    class Meta:
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.article_subcategory


class Tag(models.Model):
    article_tag = models.CharField(max_length=255, unique=True)
    tag_slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.tag_slug


class Article(models.Model):
    meta_title = models.CharField(max_length=255)
    article_header_image_url = models.CharField(max_length=255)
    article_description = models.TextField()
    article_title = models.CharField(max_length=255)
    article_content = models.TextField()
    article_published = models.DateTimeField(verbose_name="date published",
                                            )
    article_subcategory = models.ForeignKey(ArticleSubCategory,
                                            verbose_name="Sub Category",
                                            on_delete=models.CASCADE
                                            )
    article_slug = models.SlugField(max_length=255,
                                    unique=True)
    article_tags = models.ManyToManyField(Tag)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.article_title

    def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.article_slug})


class Image(models.Model):
    name_image = models.CharField(max_length=255, default='image')
    image = models.ImageField()

    def __str__(self):
        return str(self.name_image)


class CloudMessagingUser(models.Model):
    cm_token = models.CharField(max_length=255)
    cm_ip = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)