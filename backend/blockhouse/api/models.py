from django.db import models

# Create your models here.
class barGraphData(models.Model):
    labels = models.JSONField(blank=False, null=False)
    data = models.JSONField(blank=False, null=False)

class lineChartData(models.Model):
    labels = models.JSONField(blank=False, null=False)
    data = models.JSONField(blank=False, null=False)

class pieChartData(models.Model):
    labels = models.JSONField(blank=False, null=False)
    data = models.JSONField(blank=False, null=False)

class candleChartData(models.Model):
    data = models.JSONField(blank=False, null=False)
