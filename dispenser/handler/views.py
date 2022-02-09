
from os import lseek
from tkinter.tix import Tree
from django import views
from django.shortcuts import render
from data.models import File
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DataSerializer ,DataGroupSerializer,DataTestSerializer,DataTestSerializer2,DataTestSerializer3
from rest_framework import filters
from .filters import DynamicSearchFilter
from dateutil.parser import parse
from django.db.models import Count,Sum
from django.db.models import CharField, Count
from django.db.models.functions import Lower
import pandas as pd



class DataAPIView(APIView):
    
    def get(self,request,format=None):

        sortBy = self.request.query_params.get('sortBy',None)
        orderBy = self.request.query_params.get('orderBy',None)
        sortByField = self.request.query_params.get('sortByField',None)
        operation = self.request.query_params.get('operation',None)
        country = self.request.query_params.get('country',None)
        channel = self.request.query_params.get('channel',None)
        os = self.request.query_params.get('os',None)
        fromDate = self.request.query_params.get('fromDate',None)
        toDate = self.request.query_params.get('toDate',None)
        date = self.request.query_params.get('date',None)


        if operation =='filterByDater':
            response  = File.objects.filter(transaction_date__gte=fromDate,transaction_date__lte=toDate)
            serializer =DataSerializer(response ,many=Tree)
            return Response(serializer.data)
            #http://127.0.0.1:8000/adjust/?operation=filterByDater&fromDate=2017-05-17&toDate=2017-05-20

            
        if operation == 'filterByDate':
            response  = File.objects.filter(transaction_date=date)
            serializer =DataSerializer(response ,many=Tree)
            return Response(serializer.data)
            #http://127.0.0.1:8000/adjust/?operation=filterByDate&date=2017-05-17


        if operation == 'filterBychannel':
            response  = File.objects.filter(channel=channel)
            serializer =DataSerializer(response ,many=Tree)
            return Response(serializer.data)
            #http://127.0.0.1:8000/adjust/?operation=filterBychannel&channel=adcolony


       
        if operation == 'filterBycountries':
            response  = File.objects.filter(country=country)
            serializer =DataSerializer(response ,many=Tree)
            return Response(serializer.data)
            #http://127.0.0.1:8000/adjust/?operation=filterBycountries&country=US

        if operation == 'filterbyOs':
            response  = File.objects.filter(os=os)
            serializer =DataSerializer(response ,many=Tree)
            return Response(serializer.data)
            #http://127.0.0.1:8000/adjust/?operation=filterbyOs&os=ios


        if operation == 'groupbyChannel':
            response=File.objects.values('channel').annotate(clicks=Sum('clicks'))
            serializer = DataGroupSerializer(response,many =True)
            return  Response(serializer.data)
            #http://127.0.0.1:8000/adjust/?operation=groupbyChannel



        if operation == 'sortColumn':
            if sortBy == 'asc':
                response = File.objects.all().order_by(orderBy)
                serializer = DataSerializer(response,many =True)
                return  Response(serializer.data)
                #http://127.0.0.1:8000/adjust/?operation=sortColumn&sortBy=asc&orderBy=clicks

            if sortBy == 'dsc':
                response = File.objects.all().order_by(f'-{orderBy}')
                serializer = DataSerializer(response,many =True)
                return  Response(serializer.data)
                #http://127.0.0.1:8000/adjust/?operation=sortColumn&sortBy=dsc&orderBy=impressions

        if operation == 'alpha':
            response = File.objects.values('channel','country','transaction_date').filter(transaction_date=toDate).annotate(clicks = Sum('clicks'),impressions = Sum('impressions')).order_by('-clicks')
            serializer =  DataTestSerializer(response,many =True)
            return Response(serializer.data)
            #http://127.0.0.1:8000/adjust/?operation=alpha&toDate=2017-05-22



        if operation == 'beta':
            response = File.objects.values('country','os').annotate(installs = Sum('installs')).filter(transaction_date=date,os=os).order_by('transaction_date')
            serializer =  DataTestSerializer2(response,many =True)
            return Response(serializer.data)
            #http://127.0.0.1:8000/adjust/?operation=beta&date=2017-05-17&os=ios

        if operation == 'gamma':
            response = File.objects.values('revenue','os','country').annotate(installs = Sum('revenue')).filter(transaction_date=date,country=country,os=os).order_by('-revenue')
            serializer =  DataTestSerializer3(response,many =True)
            return Response(serializer.data)
            #http://127.0.0.1:8000/adjust/?operation=gamma&date=2017-05-17&country=US&os=ios

        if operation == 'delta':
            response = File.objects.values('revenue','os','country').annotate(installs = Sum('revenue')).filter(transaction_date=date,country=country,os=os).order_by('-revenue')
            serializer =  DataTestSerializer3(response,many =True)
            return Response(serializer.data)
            #http://127.0.0.1:8000/adjust/?operation=delta&date=2017-05-17&country=US&os=ios

        if operation == 'omicron':
            response = File.objects.all().annotate(cpi = ('spend'/'installs') )
            serializer =  DataSerializer(response,many =True)
            return Response(serializer.data)
            #http://127.0.0.1:8000/adjust/?operation=omicron


            



        





        


            

