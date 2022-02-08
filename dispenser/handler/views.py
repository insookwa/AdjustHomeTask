
from django.shortcuts import render
from data.models import File
from rest_framework import generics
from .serializers import DataSerializer
from rest_framework import filters
from .filters import DynamicSearchFilter
from dateutil.parser import parse



class DataAPIView(generics.ListCreateAPIView):
    serializer_class = DataSerializer
    filter_backends = (DynamicSearchFilter,)


    def get_queryset(self):  
        country = self.request.query_params.get('country',None)
        channel = self.request.query_params.get('channel',None)
        os = self.request.query_params.get('os',None)
        fromDate = self.request.query_params.get('fromDate',None)
        toDate = self.request.query_params.get('toDate',None)
        response  = File.objects.filter(country=country,channel=channel,os=os,date__gte=fromDate,date__lte=toDate)
        return response



    
     


    