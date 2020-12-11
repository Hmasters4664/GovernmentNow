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

from .serializers import TicketSerializer, TicketCommentSerializer

from Profile.models import Profile
from .models import Ticket, TicketComment


class CreateTicketView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serialized = TicketSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save(requester=request.user.profile)
            content = {'status': 'Ok'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class TicketCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        ticketid = self.request.GET.get('pk', '')
        ticket = get_object_or_404(Ticket, pk=ticketid)
        serialized = TicketCommentSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save(commenter=request.user.profile, ticket=ticket)
            content = {'status': 'Ok'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class GetTicketsByMe(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer

    def get_queryset(self):
        pk = self.request.GET.get('pk', '')
        me = get_object_or_404(Profile, pk=pk)

        return Ticket.objects.filter(requester=me)


class GetTicketsByArea(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer

    def get_queryset(self):
        suburb = self.request.GET.get('suburb', '')
        return Ticket.objects.filter(suburb=suburb)


class ResolveTicket(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if self.request.user.MunicipalProfile:
            ticketid = self.request.GET.get('pk', '')
            ticket = get_object_or_404(Ticket, pk=ticketid)
            ticket.done = True
            ticket.date_completed = datetime.today().date()
            ticket.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
