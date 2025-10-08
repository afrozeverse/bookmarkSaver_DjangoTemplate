from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Bookmarks(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField( max_length=50)
    link = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user)

