from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Application, Documents


class ApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'user', 'type', 'gender', 'race', 'birth_date', 'identification_number', 'street',
                  'date_created')


class DocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = 'file'
