from django.contrib import admin
from django.template.loader import get_template
from django.utils.translation import gettext as _

# Register your models here.
from front import models
from django.utils.safestring import mark_safe
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from front.forms import ShowAdminArticleForm, ShowAdminBlagodarnostiForm


class ArticleKindAdmin(admin.ModelAdmin):
    list_display = ['kind', 'pk']
    list_display_links = ['kind']

class ShowAPhotoInline(admin.TabularInline):
    model = models.APhoto
    fields = ("showphoto_thumbnail",)
    readonly_fields = ("showphoto_thumbnail",)
    max_num = 0
    def showphoto_thumbnail(self, instance):
        tpl = get_template("front/admin/show_thumbnail.html")
        return tpl.render({"photo": instance.photo})
    showphoto_thumbnail.short_description = _("Thumbnail")

class ArticleAdmin(admin.ModelAdmin):
    def cover_tag(self, obj):
        if not (obj.pk and obj.cover):
            return ''
        return mark_safe(f'<a href="{obj.cover.url}" target="_blank"><img src="{obj.cover.url}" height="70px"/></a>')

    cover_tag.short_description = 'Обложка'
    cover_tag.allow_tags = True
    readonly_fields = ['cover_tag']

    list_display = ['pk', 'title', 'kind', 'date_publish', 'cover_tag']
    search_fields = ['title']
    list_display_links = ['pk', 'title']
    list_filter = ['kind', 'date_publish']

    form = ShowAdminArticleForm
    inlines = [ShowAPhotoInline]
    save_on_top = True

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


class ProjectsAdmin(admin.ModelAdmin):
    def logo_tag(self, obj):
        if not (obj.pk and obj.logo):
            return ''
        return mark_safe(f'<a href="{obj.logo.url}" target="_blank"><img src="{obj.logo.url}" height="70px"/></a>')

    logo_tag.short_description = 'Логотип'
    logo_tag.allow_tags = True
    readonly_fields = ['logo_tag']
    list_display = ['pk', 'title', 'order', 'logo_tag', 'color', 'photo_amount']
    list_display_links = ['pk', 'title']
    list_editable = ['order', 'photo_amount']
    search_fields = ['title']
    save_on_top = True


class ShowBPhotoInline(admin.TabularInline):
    model = models.BPhoto
    fields = ("showphoto_thumbnail",)
    readonly_fields = ("showphoto_thumbnail",)
    max_num = 0
    def showphoto_thumbnail(self, instance):
        tpl = get_template("front/admin/show_thumbnail.html")
        return tpl.render({"photo": instance.photo})
    showphoto_thumbnail.short_description = _("Thumbnail")


class BlagodarnostiAdmin(admin.ModelAdmin):
    list_display = ['year']
    list_display_links = ['year']
    list_filter = ['year']

    form = ShowAdminBlagodarnostiForm
    inlines = [ShowBPhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)

class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'file', 'date_create']
    list_display_links = ['title']
    list_filter = ['date_create']
    search_fields = ['title']
    readonly_fields = ['date_create']


class SettingsAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ['contact_email', 'mailto', 'contact_phone', 'banner_text']
    list_display_links = ['contact_email']
    list_editable = ['contact_phone', 'banner_text']
    save_on_top = True

admin.site.register(models.ArticleKind, ArticleKindAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Projects, ProjectsAdmin)
admin.site.register(models.Blagodarnosti, BlagodarnostiAdmin)
admin.site.register(models.Documents, DocumentsAdmin)
admin.site.register(models.Settings, SettingsAdmin)