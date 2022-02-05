from .models import MenuItem
from .models import Social

def check_menu_items(get_response):
    def middleware(request, *args, **kwargs):
            request.menuitems = MenuItem.objects.all()
            request.social = Social.objects.all()
            response = get_response(request, *args, **kwargs)
            return response
    return middleware

def check_menu_items_class(get_response):
    def middleware(self, request, *args, **kwargs):
            request.menuitems = MenuItem.objects.all()
            request.social = Social.objects.all()
            response = get_response(self, request, *args, **kwargs)
            return response
    return middleware
