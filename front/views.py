from django.shortcuts import render

# Create your views here.
from django.views import View


class Index(View):
    def get(self, request):
        #todo бегущая строка settings/home
        #todo текст о нас
        #todo проекты с выбором фона, лого, заголовка и текста
        #todo три последние новости всех категорий кроме реабилитации Lenta
        #todo телефон, почта, адрес из settings
        #todo реквизиты
        return render(request, 'index.html', context={})


class About(View):
    def get(self, request):
        # todo возможно подгрузка фото из базы?
        return render(request, 'about.html', context={})

class Project(View):
    def get(self, request, project_id):
        # todo подгрузка лого, названия и описания с цветом (для главной)
        context = {'project_id': project_id,
                   'photos':[], 'description':''}
        return render(request, 'project.html', context={})

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
        return render(request, 'article.html', context={})

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