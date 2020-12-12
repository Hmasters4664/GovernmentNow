from django.contrib.auth.models import User
from rest_framework import serializers

from Profile.models import Profile
from .models import CityComplaintData, CityRanking, CitySolutionFixing


class CityComplaintDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityComplaintData
        fields = '__all__'


class CitySolutionFixingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitySolutionFixing
        fields = '__all__'


class CityRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityRanking
        fields = '__all__'
