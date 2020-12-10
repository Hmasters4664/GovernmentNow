from django.contrib.auth.models import User
from rest_framework import serializers

from Profile.models import Profile
from .models import Ticket


class ProfileSerializer(serializers.ModelSerializer):
    gender_name = serializers.CharField(source='get_gender_display', read_only=True)
    race_name = serializers.CharField(source='get_race_display', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'name', 'gender', 'race', 'gender_name', 'race_name',
                  'contact', 'birth_date', 'picture_url', 'identification_number')
        read_only_fields = ('user',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'profile', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user, **profile_data)
        return user


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'issue', 'description', 'province', 'city', 'suburb', 'street',
                  'date_created')
