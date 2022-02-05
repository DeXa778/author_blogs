from django.contrib import admin
from .models import Message
from .models import Social
from .models import MenuItem


admin.site.register(Message)
admin.site.register(Social)
admin.site.register(MenuItem)
