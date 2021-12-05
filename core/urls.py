
from django.urls import path, include

from core import views
from core.views import Index

urlpatterns = [

    path('index/' , Index,name='index'),
path('send_email/',views.send_email,name='send_email')
]