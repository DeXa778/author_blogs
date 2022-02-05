from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from .models import Social
from blog.models import Article
from blog.models import Author
from django.shortcuts import redirect
from .models import MenuItem
from blog.forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .middleware import check_menu_items_class


menu = MenuItem.objects.all()
social = Social.objects.all()

def get_message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        message = Message(name = name,email=email,message=message)
        message.save()
        return redirect('thanks')
    return redirect('main_page')


def thanks(request):
    return render(request,'thanks.html',context={'socials':social, 'menuitems':menu})

class Create_Article(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = Article
    form_class = ArticleForm
    template_name = "create.html"
    success_url = '/thanks/'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the змінних
        return context
    @check_menu_items_class
    def dispatch(self, args, **kwargs):
        return super().dispatch(args, **kwargs)
