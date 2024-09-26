from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.barGraphData)
admin.site.register(models.lineChartData)
admin.site.register(models.pieChartData)
admin.site.register(models.candleChartData)