from django.urls import re_path, path, include

from front import views, ajax
urlpatterns = [
    path('', views.Index.as_view()),
    path('about', views.About.as_view()),
    path('project/<int:project_id>', views.Project.as_view()),
    path('blagodarnosti', views.Blagodarnosti.as_view()),
    path('news/<int:category_id>', views.News.as_view()),
    path('article/<int:category_id>-<int:article_id>', views.Article.as_view()),
    path('documents', views.Documents.as_view()),
    path('rehab-program', views.RehabProgram.as_view()),
    path('rehab-zavisimosti', views.RehabVidyZavisimosti.as_view()),
    path('rehab-sozavisimost', views.RehabSozavisimost.as_view()),
    path('rehab-pamyatki', views.RehabPamyatki.as_view()),
    path('feedback/', ajax.Feedback.as_view()),
    path('login/', views.Login.as_view()),
    path('othere/', views.OthereRender.as_view()),
    path('taxi/', views.TaxiRender.as_view()),
]

