from django.conf.urls import url
from django.urls import include, re_path, path
from Ticketing import views
from .views import CreateCityComplaints, CreateCitySolutionFixing, CreateCityRankingSerializer, GetCitySolutionFixing,\
GetCityRanking, GetCityComplaintData


urlpatterns = [
    path('dashboard/create-complaints', CreateCityComplaints.as_view(), name='create-complaints'),
    path('dashboard/create-solution', CreateCitySolutionFixing.as_view(), name='create-solution'),
    path('dashboard/create-ranking', CreateCityRankingSerializer.as_view(), name='create-ranking'),
    path('dashboard/solution', GetCitySolutionFixing.as_view(), name='city-solution'),
    path('dashboard/ranking', GetCityRanking.as_view(), name='city-ranking'),
    path('dashboard/complaints', GetCityComplaintData.as_view(), name='city-complaints'),
]
