from django.urls import path
from . import views

app_name = 'blog_app'

urlspatterns=[
    #Home page
    path('', views.index, name = 'index'),
]