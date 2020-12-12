from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
from datetime import *
from dateutil.relativedelta import *
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from Profile.models import Profile
import uuid

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

ID = 0
PASSPORT = 1
SOCIAL = 2
DOCTYPE = (
    (ID, 'Identity Document'),
    (PASSPORT, 'Passport'),
    (SOCIAL, 'Social Grant Card'),
)

ERROR = 0
ACCEPTED = 1
COMPLETE = 2
INCOMPLETE = 3
STATUS = (
    (ERROR, 'ERROR'),
    (ACCEPTED, 'ACCEPTED'),
    (COMPLETE, 'COMPLETE'),
    (INCOMPLETE, 'INCOMPLETE'),
)


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=150, blank=False, )
    gender = models.IntegerField(choices=GENDER, default='Undefined')
    race = models.IntegerField(choices=RACE, default='Undefined')
    type = models.IntegerField(choices=DOCTYPE, default='Identity Document')
    status = models.IntegerField(choices=STATUS, default=3)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)
    birth_date = models.DateField(null=True, blank=True, )
    identification_number = models.CharField(max_length=25,blank=False, )
    message = models.CharField(max_length=100, unique=False, blank=True, )
    has_docs = models.BooleanField(default=True)
    date_created = models.DateField(auto_now=True)


class Documents(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=False)
    file = models.FileField(upload_to='documents')
    date_submitted = models.DateField(auto_now_add=True, blank=True, )
