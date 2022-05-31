from django.http import HttpResponse
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import *
from .serializers import *
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class DataList(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    name = 'data-list'
    search_fields = ['money']

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    name = 'data-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self,request,*args,**kwargs):
        return Response({
            'status': 'request was permitted',
            'clients': reverse(DataList.name,request=request),
        })