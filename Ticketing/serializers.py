from django.contrib.auth.models import User
from rest_framework import serializers

from Profile.models import Profile
from .models import Ticket, TicketComment


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'issue', 'description', 'province', 'city', 'suburb', 'street',
                  'date_created')


class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('comment', 'commenter')
