import os
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.conf import settings as base_conf
import random

from front import models


def make_context(**kwargs):
    try:
        settings = models.Settings.objects.get()
    except:
        context = {}
    else:
        context = {'settings': settings}
    if kwargs:
        for k, v in kwargs.items():
            context[f'{k}'] = v
    return context


class Index(View):
    def get(self, request):
        projects3 = models.Projects.objects.all()[:3]
        projects4 = models.Projects.objects.all()[3:7]
        news = models.Article.objects.all().filter(kind__pk__in=range(1, 3)).order_by("-date_publish")[:3]
        context = make_context(news=news,
                               projects3=projects3,
                               projects4=projects4,
                               )
        return render(request, 'index.html', context=context)


class About(View):
    def get(self, request):
        # todo возможно подгрузка фото из базы?
        return render(request, 'about.html', context={})


class Project(View):
    def get(self, request, project_id):
        # todo подгрузка лого, названия и описания
        project = models.Projects.objects.filter(pk=project_id).first()
        if not project:
            return HttpResponseRedirect('/')
        BASE_DIR = base_conf.BASE_DIR
        photos = os.listdir(os.path.join(BASE_DIR, 'static', 'images', 'projects', f'{project.pk}'))
        if photos:
            cover =sorted(photos)[0]
            random.shuffle(photos)
            if len(photos) >= project.photo_amount:
                photos_part = photos[:project.photo_amount]
            else:
                photos_part = photos
        else:
            photos_part = []
            cover = None
        context = make_context(project=project,
                               photos=photos_part,
                               cover=cover)
        return render(request, 'project.html', context=context)


class Blagodarnosti(View):
    def get(self, request):
        # todo подгрузка фото из базы по годам
        return render(request, 'blagodarnosti.html', context={})


class News(View):
    def get(self, request, category_id):
        # todo функционал
        # todo функционал под реабилитацию
        return render(request, 'news.html', context={})
        # todo return render(request, 'reability_news.html', context={})


class Article(View):
    def get(self, request, category_id, article_id):
        # todo функционал
        # todo функционал под реабилитацию
        article = models.Article.objects.filter(kind__pk=category_id,
                                                pk=article_id).first()
        context = make_context(article=article)
        if article:
            return render(request, 'article.html', context=context)
        else:
            HttpResponseRedirect('/')


class Documents(View):
    def get(self, request):
        # todo функционал добавления доков в базу по дате
        return render(request, 'documents.html', context={})


class RehabProgram(View):
    def get(self, request):
        return render(request, 'reability.html', context={})


class RehabVidyZavisimosti(View):
    def get(self, request):
        return render(request, 'vidy_zavisimosti.html', context={})


class RehabSozavisimost(View):
    def get(self, request):
        return render(request, 'sozavisimost.html', context={})


class RehabPamyatki(View):
    def get(self, request):
        return render(request, 'pamyatki.html', context={})
