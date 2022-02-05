from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .models import Author
from connection.models import Social
from connection.models import MenuItem
from django.views.generic.edit import CreateView
from .forms import ArticleForm
from .middleware import check_articles
from connection.middleware import check_menu_items_class
from django.contrib.auth.mixins import LoginRequiredMixin
from connection.middleware import check_menu_items

 

@check_menu_items
@check_articles
def index(request):
    return render(request, 'index.html', context={'articles':Article.objects.all()})

@check_menu_items
def author_page(request, id):
    return render(request, 'author.html', context={'author':Author.objects.get(id=id)})

@check_menu_items
def article_page(request, id):
    return render(request, 'article.html', context={'article':Article.objects.get(id=id)})

@check_menu_items
def test_page(request):
    return render(request,"tmp.html", context={"name":"DIMKA"})


class Create_Article(LoginRequiredMixin,CreateView): # клас який відповідає за створення статей
    login_url = '/auth/login/' # шлях на який переводимо якщо не зареєстровані
    model = Article # кажемо що будемо створювати статті
    template_name = 'create.html' # сторінка де знаходиться форма
    form_class = ArticleForm    # форма яка буде відображатись у змінній form
    success_url = '/thanks/'    # після успішного надсилання перейде за цією адресою

    def get_context_data(self, kwargs):   # дія додаткового контенту
        context = super().get_context_data(kwargs) # отримує форму і дані моделі
        return context


    @check_menu_items_class
    def dispatch(self, args, **kwargs):
        return super().dispatch(args, **kwargs)

'''
def create_article(request):
    if request.method == "POST":
        article = Article() # створення статті
        #request.POST набір даних із запиту
        # вказати поля
        article.title = request.POST['title'] # отримання даних з поля title
        article.text = request.POST['text'] # отримання даних з поля text
        article.image = request.POST['image'] # отримання даних з поля image
        article.publication = request.POST['publication'] # отримання даних з поля дати і часу
        article.save()

        author_id = int(request.POST['author']) # НОМЕР АВТОРА ЯКИЙ НАМ ПОТРІБЕН
        author = Author.objects.get(id=author_id) # знаходимо автора за номером
        article.author.add(author) # додати автора статті
        article.save() # зберігаємо зміни

    return render(request,'create.html',context={'authors':Author.objects.all()})
'''
