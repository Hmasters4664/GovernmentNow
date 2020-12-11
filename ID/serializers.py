from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Application, Documents


class ApplicationSerializers(serializers.ModelSerializer):
    gender_name = serializers.CharField(source='get_gender_display', read_only=True)
    race_name = serializers.CharField(source='get_race_display', read_only=True)
    type_name = serializers.CharField(source='get_type_display', read_only=True)
    status_name = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Application
        fields = ('id', 'name', 'status', 'type', 'status_name', 'type_name', 'gender_name', 'race_name'
                  , 'gender', 'race', 'birth_date', 'identification_number',
                  'date_created')


class DocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ('id','file')
