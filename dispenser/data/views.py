from django.shortcuts import render
from rest_framework import status
from django.shortcuts import render
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from .models import File
from .serializers import FileUploadSerializer, SaveFileSerializer

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = File(
                    date = row['date'],
                    channel = row['channel'],
                    country = row['country'],
                    os = row['os'],
                    impressions = row['impressions'],
                    clicks = row['clicks'],
                    installs = row['installs'],
                    spend = row['spend'],
                    revenue = row['revenue'],
                       )
            new_file.save()
        return Response({"status": "success"}, status = status.HTTP_201_CREATED)
