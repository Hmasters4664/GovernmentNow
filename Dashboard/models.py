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
import os


class CityComplaintData(models.Model):
    cityname = models.CharField(max_length=150, blank=False)
    water = models.IntegerField(blank=False, )
    infrastructure = models.IntegerField(blank=False, )
    education = models.IntegerField(blank=False, )
    electricity = models.IntegerField(blank=False, )
    housing = models.IntegerField(blank=False, )


class CitySolutionFixing(models.Model):
    cityname = models.CharField(max_length=150, blank=False)
    water_time = models.IntegerField(blank=False, )
    infrastructure_time = models.IntegerField(blank=False, )
    education_time = models.IntegerField(blank=False, )
    electricity_time = models.IntegerField(blank=False, )
    housing_time = models.IntegerField(blank=False, )


class CityRanking(models.Model):
    cityname = models.CharField(max_length=150, blank=False)
    rank = models.IntegerField(blank=False, )