from django.db import models
from django.utils import timezone
from datetime import datetime

class Todo(models.Model):
    item = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.item
