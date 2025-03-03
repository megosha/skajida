import os

from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.
from django.views import View
from django.conf import settings as base_conf
import random

from front import models, forms


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
        news = models.Article.objects.all().filter(kind__pk__in=range(1, 4), date_publish__lte=timezone.now()).order_by(
            "-date_publish")[:3]
        context = make_context(news=news,
                               projects3=projects3,
                               projects4=projects4,
                               )
        return render(request, 'index.html', context=context)


class About(View):
    def get(self, request):
        context = make_context()
        return render(request, 'about.html', context=context)


class Project(View):
    def get(self, request, project_id):
        project = models.Projects.objects.filter(pk=project_id).first()
        if not project:
            return HttpResponseRedirect('/')
        BASE_DIR = base_conf.BASE_DIR
        photos = os.listdir(os.path.join(BASE_DIR, 'static', 'images', 'projects', f'{project.pk}'))
        if photos:
            cover = sorted(photos)[0]
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
        photos = models.BPhoto.objects.all().order_by("year")
        context = make_context(photos=photos)
        return render(request, 'blagodarnosti.html', context=context)


class News(View):
    def get(self, request, category_id):
        kinds = models.ArticleKind.objects.all()
        kinds_pk = list(kinds.values_list('pk', flat=True))
        if category_id in kinds_pk:
            current_category = kinds.filter(pk=category_id).first()
            news = models.Article.objects.filter(kind__pk=category_id, date_publish__lte=timezone.now()).order_by(
                "-date_publish")
        else:
            current_category = None
            news = models.Article.objects.filter(kind__pk__in=range(1, 4), date_publish__lte=timezone.now()).order_by("-date_publish")
        paginator = Paginator(news, 10)
        page = request.GET.get('page')
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            news = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            news = paginator.page(paginator.num_pages)
        context = make_context(kinds=kinds,
                               current_category=current_category,
                               news=news,
                               page=page)
        request.session['return_page'] = f'{page}'
        request.session['return_category'] = f'{category_id}'
        return render(request, 'news.html', context=context)


class Article(View):
    def get(self, request, category_id, article_id):
        article = models.Article.objects.filter(kind__pk=category_id, pk=article_id,
                                                date_publish__lte=timezone.now()).first()
        if not article:
            return HttpResponseRedirect('/')
        photos = models.APhoto.objects.filter(article__pk=article_id)
        return_page = request.session.pop('return_page') if 'return_page' in request.session else 0
        return_category = request.session.pop('return_category') if 'return_category' in request.session else 0
        if category_id == 4:
            next_article = models.Article.objects.filter(date_publish__gt=article.date_publish,
                                                         date_publish__lte=timezone.now(),
                                                         kind__pk=category_id).order_by('date_publish').first()
            prev_article = models.Article.objects.filter(date_publish__lt=article.date_publish,
                                                         date_publish__lte=timezone.now(),
                                                         kind__pk=category_id).order_by('date_publish').last()
        else:
            next_article = models.Article.objects.filter(date_publish__gt=article.date_publish,
                                                     date_publish__lte=timezone.now(),
                                                     kind__pk__in=range(1,4)).order_by('date_publish').first()
            prev_article = models.Article.objects.filter(date_publish__lt=article.date_publish,
                                                     date_publish__lte=timezone.now(),
                                                     kind__pk__in=range(1,4)).order_by('date_publish').last()

        context = make_context(article=article,
                               photos=photos,
                               next_article=next_article,
                               prev_article=prev_article,
                               return_page=return_page,
                               return_category=return_category
                               )
        return render(request, 'article.html', context=context)


class Documents(View):
    def get(self, request):
        files = models.Documents.objects.all().order_by("date_create")
        context = make_context(files=files)
        return render(request, 'documents.html', context=context)


class RehabProgram(View):
    def get(self, request):
        context = make_context()
        return render(request, 'reability.html', context=context)


class RehabVidyZavisimosti(View):
    def get(self, request):
        context = make_context()
        return render(request, 'vidy_zavisimosti.html', context=context)


class RehabSozavisimost(View):
    def get(self, request):
        context = make_context()
        return render(request, 'sozavisimost.html', context=context)


class RehabPamyatki(View):
    def get(self, request):
        context = make_context()
        return render(request, 'pamyatki.html', context=context)

class Login(View):
    def dispatch(self, request, *args, **kwargs):
        try:
            if self.request.user.is_authenticated:
                return HttpResponseRedirect('/admin_sjd/')
            else:
                return super(Login, self).dispatch(request)
        except:
            return HttpResponseRedirect('/login')

    def get(self, request):
        form = forms.Login()
        context = make_context(form=form)
        return render(request, 'login.html', context)

    def post(self, request):
        form = forms.Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            pwd = form.cleaned_data['pwd']
            try:
                user = authenticate(username=username, password=pwd)
            except Exception as e:
                print(e)
                return self.get(request)
            login(self.request, user)
            print(user)
            return HttpResponseRedirect('/admin_sjd')
        return HttpResponseRedirect('/')


class Logout(View):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return HttpResponseRedirect('/')

def notfound(request, exception=None):
    return redirect('/')

class OthereRender(View):
    def get(self, request):
        return render(request, 'othere.html', context=make_context())


class TaxiRender(View):
    def get(self, request):
        return render(request, 'taxi.html', context=make_context())
