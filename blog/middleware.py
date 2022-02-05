from .models import Article
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from connection.models import Social
from connection.models import MenuItem



menu = MenuItem.objects.all()
social = Social.objects.all()


def check_articles(get_response):
    def middleware(request):
        if len(Article.objects.all()) > 0:   
            response = get_response(request)
        else:
            return render(request, 'sorry.html', context={'socials':social,'menuitems':menu})
        return response

    return middleware




