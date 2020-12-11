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

from .models import Application, Documents
from Profile.models import Profile
from .serializers import ApplicationSerializers, DocumentsSerializers


class CreateApplicationView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serialized = ApplicationSerializers(data=request.data)
        if serialized.is_valid():
            serialized.save(user=request.user.profile)
            content = {'status': 'Ok'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        applicationID = self.request.GET.get('pk', '')
        application = get_object_or_404(Application, pk=applicationID)

        file_serializer = DocumentsSerializers(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save(application=application)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
