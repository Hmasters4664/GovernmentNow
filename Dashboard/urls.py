from django.conf.urls import url
from django.urls import include, re_path, path
from Ticketing import views
from .views import CreateCityComplaints, CreateCitySolutionFixing, CreateCityRankingSerializer, GetCitySolutionFixing,\
GetCityRanking, GetCityComplaintData, Dashboard


urlpatterns = [
    path('dashboard/create-complaints', CreateCityComplaints.as_view(), name='create-complaints'),
    path('dashboard/create-solution', CreateCitySolutionFixing.as_view(), name='create-solution'),
    path('dashboard/create-ranking', CreateCityRankingSerializer.as_view(), name='create-ranking'),
    path('dashboard/dashboard', Dashboard.as_view(), name='dashboard'),
]
