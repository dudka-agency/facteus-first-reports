from django.db import models


class FirstReport(models.Model):
    merchant = models.CharField(max_length=50)
