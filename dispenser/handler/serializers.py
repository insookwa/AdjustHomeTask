from rest_framework import serializers
from data.models import File

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'