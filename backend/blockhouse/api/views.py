from api.models import barGraphData, lineChartData, pieChartData, candleChartData
from api.serializers import barChartSerializer, lineChartSerializer, pieChartSerializer, candleChartSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions

# Create your views here.
def index(request):
    return HttpResponse("Home")

class BarData(ListCreateAPIView):
    queryset = barGraphData.objects.all()
    serializer_class = barChartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #Protecting from outside users inputting random models into database

class LineData(ListCreateAPIView):
    queryset = lineChartData.objects.all()
    serializer_class = lineChartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class pieData(ListCreateAPIView):
    queryset = pieChartData.objects.all()
    serializer_class = pieChartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class candleData(ListCreateAPIView):
    queryset = candleChartData
    serializer_class = lineChartData
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
