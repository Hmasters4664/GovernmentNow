import sys

from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_list_or_404, get_object_or_404
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile
from io import StringIO, BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from .validators import validate_characters, check_negative_number, check_zero_number
import os

RELATIONSHIP_FOLLOWING = 0
RELATIONSHIP_BLOCKED = 1
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Allowed'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)

FEMALE = 0
MALE = 1
UNDEFINED = 2
GENDER = (
    (FEMALE, 'Female'),
    (MALE, 'Male'),
    (UNDEFINED, 'Undefined'),
)

BLACK = 0
WHITE = 1
ARAB = 2
SE_ASIAN = 3
FE_ASIAN = 4
UNDEFINED = 5
RACE = (
    (BLACK, 'Black'),
    (WHITE, 'White'),
    (ARAB, 'Arab'),
    (SE_ASIAN, 'South East Asian'),
    (FE_ASIAN, 'Far East Asian'),
    (UNDEFINED, 'Undefined'),
)


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, validators=[validate_characters], )
    gender = models.IntegerField(choices=GENDER, default='Undefined')
    race = models.IntegerField(choices=RACE, default='Undefined')
    identification_number = models.CharField(max_length=25, unique=True)
    contact = models.CharField(max_length=12, blank=True, validators=[validate_characters], )
    birth_date = models.DateField(null=True, blank=True, )
    picture_url = models.CharField(max_length=200, default='')


class MunicipalProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, validators=[validate_characters], )
    municipality = models.CharField(max_length=100, blank=True)
    employee_number = models.CharField(max_length=25, unique=True)
    suburb = models.CharField(max_length=100, blank=True)