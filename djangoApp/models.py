from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=80)
    email = models.CharField(max_length=255)
    display_name = models.CharField(max_length=32)
    created_at = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
