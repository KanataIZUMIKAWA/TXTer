from django.db import models

# Create your models here.
from django.utils import timezone

class Posts(models.Model):
    """投稿情報"""
    user = models.CharField(default='noname', max_length=64)
    note = models.TextField(default='')
    read = models.BooleanField(default=False)