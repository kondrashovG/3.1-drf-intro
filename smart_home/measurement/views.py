# опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from .models import Sensor
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# class SensorListView(ListCreateAPIView):
#     def get(self, request):
#         print('------SensorListView-----')
#         queryset = Sensor.objects.all()
#         serializer = SensorDetailSerializer(queryset, many=True)
#         return Response(serializer.data)


class SensorListCreateView(ListCreateAPIView):
    def get(self, request):
        print('-------SensorListCreateView-------')
        queryset = Sensor.objects.all()
        serializer = SensorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementListCreateView(ListCreateAPIView):
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



