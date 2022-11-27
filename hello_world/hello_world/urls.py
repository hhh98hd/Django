from curses.ascii import HT
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(req): return HttpResponse('INDEX')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index),
    path('first_app/', include('first_app.urls'))
]

