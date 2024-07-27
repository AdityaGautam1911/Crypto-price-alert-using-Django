from django.db import models
from datetime import date
from datetime import datetime


class Alert(models.Model):
    price = models.CharField(max_length=250)
    alert_date_and_time = models.DateField()

    def __str__(self):
        return self.price
