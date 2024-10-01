from django.db import models


class invitee_data(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    startTime = models.CharField(max_length=30)
    endTime = models.CharField(max_length=30)
