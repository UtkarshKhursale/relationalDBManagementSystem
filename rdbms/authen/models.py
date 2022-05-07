from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    mobile_no = models.CharField(max_length=10, blank=False)
    branch = models.CharField(max_length=100, blank=False)
    batch = models.PositiveIntegerField(null=False, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
