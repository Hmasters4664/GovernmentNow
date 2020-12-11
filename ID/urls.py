from django.conf.urls import url
from django.urls import include, re_path, path
from Ticketing import views
from .views import CreateApplicationView,FileUploadView, MyApplications


urlpatterns = [
    path('apply/new', CreateApplicationView.as_view(), name='apply'),
    path('apply/upload', FileUploadView.as_view(), name='application-files'),
    path('apply/myapplications', MyApplications.as_view(), name='applications'),
]
