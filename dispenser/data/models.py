from django.db import models
from django.forms import FloatField

class File(models.Model):

    transaction_date = models.DateField()
    channel = models.CharField(max_length=100)
    country = models.CharField(max_length=10)
    os = models.CharField(max_length=20)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()

    def __str__(self):
        return self.channel