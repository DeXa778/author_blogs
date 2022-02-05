from django.urls import path

from .views import index
from .views import author_page
from .views import article_page
from .views import test_page
from .views import Create_Article

urlpatterns = [
    path('', index, name='main_page'),
    path('author/<id>', author_page),
    path('article/<id>', article_page),
    path('tmp/', test_page),
    path('create/', Create_Article.as_view()),


]