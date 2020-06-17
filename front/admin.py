from django.contrib import admin

# Register your models here.
from front import models


class ArticleKindAdmin(admin.ModelAdmin):
    list_display = ['kind', 'pk']
    list_display_links = ['kind']
    # save_on_top = True

admin.site.register(models.ArticleKind, ArticleKindAdmin)