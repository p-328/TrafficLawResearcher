from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid 

# Create your models here.
class Chatbot(models.Model):
    name = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.TimeField(default=timezone.now)
    is_archived = models.BooleanField(default=False)

class GeneralQuery(models.Model):
    text = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    bot = models.ForeignKey(to=Chatbot, on_delete=models.CASCADE)
    time_created = models.TimeField(default=timezone.now)
    is_archived = models.BooleanField(default=False)

class ReportQuery(models.Model):
    criteria = models.TextField()
    type_of_data = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    bot = models.ForeignKey(to=Chatbot, on_delete=models.CASCADE)
    time_created = models.TimeField(default=timezone.now)
    is_archived = models.BooleanField(default=False)

class GeneralResponse(models.Model):
    text = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    g_query = models.OneToOneField(GeneralQuery, on_delete=models.CASCADE)
    time_created = models.TimeField(default=timezone.now)
    is_archived = models.BooleanField(default=False)

class ReportResponse(models.Model):
    text = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    file_link = models.URLField()
    r_query = models.OneToOneField(ReportQuery, on_delete=models.CASCADE)
    time_created = models.TimeField(default=timezone.now)
    is_archived = models.BooleanField(default=False)
