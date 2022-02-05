from django.urls import path, include
from .views import Create_User
from .views import login
from .views import log_out


urlpatterns = [
    path('create_user/',Create_User.as_view()),
    path('login/',login),
    path('logout/', log_out),
]