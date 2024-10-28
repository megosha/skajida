from django.urls import re_path, path, include

from front import views, ajax
urlpatterns = [
    re_path('about/?', views.About.as_view()),
    path('project/<int:project_id>', views.Project.as_view()),
    re_path('blagodarnosti/?', views.Blagodarnosti.as_view()),
    path('news/<int:category_id>', views.News.as_view()),
    path('article/<int:category_id>-<int:article_id>', views.Article.as_view()),
    re_path('documents/?', views.Documents.as_view()),
    re_path('rehab-program/?', views.RehabProgram.as_view()),
    re_path('rehab-zavisimosti/?', views.RehabVidyZavisimosti.as_view()),
    re_path('rehab-sozavisimost/?', views.RehabSozavisimost.as_view()),
    re_path('rehab-pamyatki/?', views.RehabPamyatki.as_view()),
    re_path('feedback/?', ajax.Feedback.as_view()),
    re_path('login/?', views.Login.as_view()),
    re_path('othere/?', views.OthereRender.as_view()),
    re_path('taxi/?', views.TaxiRender.as_view()),
    path('', views.Index.as_view()),
]

