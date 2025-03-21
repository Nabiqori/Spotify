from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from .models import *

class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class QoshiqchiModelViewset(viewsets.ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['ism', 'davlat']
    ordering_fields = ['t_sana']

    @action(detail=True, methods=['post'])
    def Jadvalqoshish(self, request, pk=None):
        qoshiqchi = self.get_object()
        serializer = JadvalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(qoshiqchi=qoshiqchi)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['get'])
    def Jadvallar(self, request, pk=None):
        jadval = Jadval.objects.all()
        serializer = JadvalSerializer(jadval, many=True)
        return Response(serializer.data)

class AlbomModelViewset(viewsets.ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nom']
    ordering_fields = ['sana']

    @action(detail=True, methods=['post'])
    def Albomqoshish(self, request, pk=None):
        try:
            qoshiqchi = Qoshiqchi.objects.get(pk=pk)
        except Qoshiqchi.DoesNotExist:
            return Response({"error": "Qoshiqchi topilmadi"}, status=404)

        serializer = AlbomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(qoshiqchi=qoshiqchi)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['get'])
    def Albomlar(self, request, pk=None):
        jadval = Albom.objects.all()
        serializer = AlbomSerializer(jadval, many=True)
        return Response(serializer.data)

class JadvalModelViewset(viewsets.ModelViewSet):
    queryset = Jadval.objects.all()
    serializer_class = JadvalSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nom', 'janr']
    ordering_fields = ['davomiylik']

    @action(detail=True, methods=['post'])
    def Jadvalqoshish(self, request, pk=None):
        try:
            albom = Albom.objects.get(pk=pk)
        except Albom.DoesNotExist:
            return Response({"error": "Albom topilmadi"}, status=404)

        serializer = JadvalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(albom=albom)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['get'])
    def Jadvallar(self, request, pk=None):
        jadval = Jadval.objects.all()
        serializer = JadvalSerializer(jadval, many=True)
        return Response(serializer.data)
