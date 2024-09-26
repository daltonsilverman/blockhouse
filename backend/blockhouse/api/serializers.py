from rest_framework import serializers
from api.models import barGraphData, lineChartData, pieChartData, candleChartData

class barChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = barGraphData
        fields = ['labels', 'data']

class lineChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = lineChartData
        fields = ['labels', 'data']

class pieChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = pieChartData
        fields = ['labels', 'data']

class candleChartSerializer(serializers.ModelSerializer):
    class Meta:
        model= candleChartData
        fields = ['data']
    