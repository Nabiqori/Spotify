from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from .models import *

# class QoshiqchilarAPIView(APIView):
#     def get(self, request):
#         serializer = QoshiqchiSerializer(Qoshiqchi.objects.all(), many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = QoshiqchiSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#     def put(self, request, pk):
#         qoshiqchi = Qoshiqchi.objects.get(pk=pk)
#         serializer = QoshiqchiSerializer(qoshiqchi, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, pk):
#         try:
#             qoshiqchi = Qoshiqchi.objects.get(pk=pk)
#             qoshiqchi.delete()
#             return Response({'xabar': 'Qoshiqchi muvaffaqiyatli o‘chirildi'}, status=204)
#         except Qoshiqchi.DoesNotExist:
#             return Response({'xato': 'Qoshiqchi topilmadi'}, status=404)
#
# class JadvallarAPIView(APIView):
#     def get(self, request):
#         serializer = JadvalSerializer(Jadval.objects.all(), many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = JadvalSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#     def put(self, request, pk):
#         qoshiqchi = Jadval.objects.get(pk=pk)
#         serializer = JadvalSerializer(qoshiqchi, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, pk):
#         try:
#             jadval = Jadval.objects.get(pk=pk)
#             jadval.delete()
#             return Response({'xabar': 'Jadval muvaffaqiyatli o‘chirildi'}, status=204)
#         except Jadval.DoesNotExist:
#             return Response({'xato': 'Jadval topilmadi'}, status=404)
class QoshiqchiModelViewset(viewsets.ModelViewSet):
    queryset = Qoshiqchi.objects.all()

    def get_serializer_class(self):
        if self.action == 'Jadvalqoshish':
            return JadvalSerializer
        return QoshiqchiSerializer

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

    @action(detail=True, methods=['get'])
    def qoshiqchilar(self, request, pk=None):
        qoshiqchi = Qoshiqchi.objects.all()
        serializer = QoshiqchiSerializer(qoshiqchi, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def Albomlar(self, request, pk=None):
        albom = Albom.objects.all()
        serializer = AlbomSerializer(albom, many=True)
        return Response(serializer.data)

class AlbomModelViewset(viewsets.ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

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

    @action(detail=True, methods=['get'])
    def Jadvallar(self, request, pk=None):
        albom=self.get_object()
        jadval = Jadval.objects.filter(albom=albom)
        serializer = JadvalSerializer(jadval, many=True)
        return Response(serializer.data)
class JadvalModelViewset(viewsets.ModelViewSet):
    queryset = Jadval.objects.all()
    serializer_class = JadvalSerializer

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
