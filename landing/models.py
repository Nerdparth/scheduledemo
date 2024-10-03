from django.db import models

class PreBooking(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=10)
