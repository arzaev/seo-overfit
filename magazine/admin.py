from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Article, ArticleCategory, ArticleSubCategory, Tag, Image, CloudMessagingUser


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_title', 'article_slug', 'is_public')
    fieldsets = [
        ("Meta", {"fields": ["meta_title"]}),
        ("Title/date", {"fields": ["article_slug",
                                   "article_header_image_url",
                                   "article_title",
                                   "article_description",
                                   "article_published"]}),
        ("Content", {"fields": ["article_content"]}),
        ("SubCategory", {"fields": ["article_subcategory"]}),
        ("Tags", {"fields": ["article_tags"]}),
        ("Public", {"fields": ["is_public"]}),
    ]
    prepopulated_fields = {"article_slug": ("article_title", )}

    #     formfield_overrides = {
    #     models.TextField: {'widget': TinyMCE()}
    # }


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
admin.site.register(ArticleSubCategory)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(CloudMessagingUser)