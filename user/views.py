from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import login as log_user
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import UserForm
from blog.models import Author

class Create_User(CreateView):
    model = Author
    fields = ['email','password','age']
    template_name = 'create.html'
    success_url = '/thanks/'

def login(request):
    if request.method == "POST": # якщо запит був надісланицй з форми
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None: # якщо коритсувач Є

            log_user(request, user)
            print(user)
            return redirect('/')
        else:
            print("КОРИСТУВАЧА НЕМАЄ")
    return render(request, 'create.html', context={'form':UserForm})

def log_out(request):
    logout(request)
    return redirect('/thanks/')
