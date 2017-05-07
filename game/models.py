from django.db import models
from django.utils import timezone


class GameInfo(models.Model):
    session_id = models.IntegerField()
    goban_info = models.TextField()
