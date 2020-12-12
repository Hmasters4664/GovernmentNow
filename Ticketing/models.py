from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
from .validators import validate_characters
from datetime import *
from dateutil.relativedelta import *
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from Profile.models import Profile
import uuid

EDUCATION = 0
ELECTRICITY = 1
WATER = 2
HOUSING = 3
INFRASTRUCTURE = 4
TYPE = (
    (EDUCATION, 'EDUCATION'),
    (ELECTRICITY, 'ELECTRICITY'),
    (WATER, 'WATER & SANITATION'),
    (HOUSING, 'HOUSING'),
    (INFRASTRUCTURE, 'INFRASTRUCTURE'),
)


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    issue = models.IntegerField(choices=TYPE, default=0)
    description = models.TextField(blank=True)
    province = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    requester = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    suburb = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=150, blank=True)
    date_created = models.DateField(auto_now=True )
    date_completed = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']


class TicketComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    commenter = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, blank=True)
    comment = models.CharField(max_length=200, blank=True)
