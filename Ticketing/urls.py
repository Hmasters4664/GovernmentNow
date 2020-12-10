from django.conf.urls import url
from django.urls import include, re_path, path
from Ticketing import views

urlpatterns = [
    path('register', views.create_user, name='register'),
]