from rest_framework import serializers
from hack_app.models import FileInformation
from hack_app.models import SensorData


class FileInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInformation
        fields = ['id', 'filename', 's3_url', 'upload_date']


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('data',)
