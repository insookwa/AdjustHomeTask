from rest_framework import serializers
from data.models import File

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class DataGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['clicks','channel']


class DataTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['channel','country','impressions','clicks','transaction_date']
        

class DataTestSerializer2(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['os','country','installs']

class DataTestSerializer3(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['os','country','revenue']

class DataTestSerializer4(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['os','country','revenue']