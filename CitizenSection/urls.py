from django.conf.urls import url
from django.urls import include, re_path, path
from CitizenSection import views

urlpatterns = [
    path('citizen/register', views.create_user, name='citizen-register'),
]