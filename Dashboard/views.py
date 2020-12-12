from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404, CreateAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from datetime import *
from dateutil.relativedelta import *
from datetime import timedelta

from .serializers import CityComplaintDataSerializer, CityRankingSerializer, CitySolutionFixingSerializer

from Profile.models import Profile
from .models import CitySolutionFixing, CityRanking, CityComplaintData


class CreateCityComplaints(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serialized = CityComplaintDataSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            content = {'status': 'Ok'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCitySolutionFixing(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serialized = CitySolutionFixingSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            content = {'status': 'Ok'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCityRankingSerializer(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serialized = CityRankingSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            content = {'status': 'Ok'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class GetCityComplaintData(generics.ListAPIView):
    serializer_class = CityComplaintDataSerializer

    def get_queryset(self):
        return CityComplaintData.objects.all()


class GetCitySolutionFixing(generics.ListAPIView):
    serializer_class = CitySolutionFixingSerializer

    def get_queryset(self):
        return CitySolutionFixing.objects.all()


class GetCityRanking(generics.ListAPIView):
    serializer_class = CityRankingSerializer

    def get_queryset(self):
        return CityRanking.objects.all()