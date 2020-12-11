from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404, CreateAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from datetime import timedelta

from Profile.serializers import UserSerializer
from Ticketing.serializers import TicketSerializer, TicketCommentSerializer

from Profile.models import Profile
from Ticketing.models import Ticket, TicketComment


@csrf_exempt
@api_view(['POST'])
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        content = {'status': 'Ok'}
        return Response(content, status=status.HTTP_200_OK)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


