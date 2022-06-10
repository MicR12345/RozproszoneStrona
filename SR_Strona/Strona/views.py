from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import *
from .serializers import *

class DataList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'video.html'
    name = 'data-list'
    def get(self,request):
        queryset = Data.objects.all()
        return Response({'data':queryset})

class Opis(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'opis.html'
    name = 'opis'
    def get(self,request):
        return Response()

class DataDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'videoDetail.html'
    name = 'data-detail'
    def get(self, request, pk):
        data = get_object_or_404(Data, pk=pk)
        serializer = DataSerializer(data)
        return Response({'serializer': serializer, 'data': data})

    def post(self, request, pk):
        data = get_object_or_404(Data, pk=pk)
        serializer = DataSerializer(data, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'data': data})
        serializer.save()
        return redirect('data-list')

    def delete(self,request,pk):
        data = get_object_or_404(Data, pk=pk)
        data.delete()
        return redirect('data-list')

class DataDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'videoDetail.html'
    name = 'data-delete'
    def post(self, request, pk):
        data = get_object_or_404(Data, pk=pk)
        data.delete()
        return redirect('data-list')

class DataAdd(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'videoAdd.html'
    name = 'data-add'
    def get(self, request):
        serializer = DataSerializer()
        return Response({'serializer': serializer})
    def post(self, request):
        data = Data()
        serializer = DataSerializer(data, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'data': data})
        serializer.save()
        return redirect('data-list')

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self,request,*args,**kwargs):
        return Response({
            'status': 'request was permitted',
            'clients': reverse(DataList.name,request=request),
        })