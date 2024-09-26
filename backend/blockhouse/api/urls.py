from django.urls import path
from . import views

# Define a list of url patterns
urlpatterns = [
    path('bar-chart-data/', views.BarData.as_view()),
    path('line-chart-data/', views.LineData.as_view()),
    path('pie-chart-data/', views.pieData.as_view()),
    path('candlestick-data/', views.candleData.as_view())
]