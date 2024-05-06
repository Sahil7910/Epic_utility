from datetime import datetime
from datetime import date
from django.db import models

# Create your models here.

class Epic (models.Model):
    today = date.today()
    month_year = today.strftime('%m-%Y')

    id=models.AutoField(primary_key=True)
    epic=models.CharField(max_length=200)
    date=models.DateTimeField(default=datetime.now, blank=True)
    manufacturerName=models.CharField(max_length=200)
    manufacturerRegistration = models.CharField(max_length=200)
    batchNo=models.CharField(max_length=200)
    monthYear_manufacture=models.DateTimeField(default=datetime.now, blank=True)
