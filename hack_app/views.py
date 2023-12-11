import os
from rest_framework.views import APIView
from rest_framework.response import Response
from hack_app.models import FileInformation
from hack_app.serializers import FileInformationSerializer
import boto3
from django.middleware.csrf import get_token
from django.http import JsonResponse
from hack_app.models import SensorData
from hack_app.serializers import SensorDataSerializer
import json
from rest_framework import status


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

class upload_to_s3(APIView):
    def post(self, request):
        credentials_file_path = 'D:/key/credentials'  # Full path to the file

        if os.path.exists(credentials_file_path):
            try:
                # AWS S3 Configuration (Ensure your environment variables are set)
                s3 = boto3.client(
                    's3',
                    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
                    region_name=os.environ.get('AWS_REGION')
                )

                # Bucket and Key (File Path) in S3
                bucket_name = 'prjctbckt'
                s3_file_path = os.path.basename(credentials_file_path)

                # Uploading file to S3
                with open(credentials_file_path, 'rb') as file:
                    s3.upload_fileobj(file, bucket_name, s3_file_path)

                # Save information to your database
                s3_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_file_path}"
                file_info = FileInformation.objects.create(
                    filename=s3_file_path,
                    s3_url=s3_url
                )

                # Serialize and return the file information
                serializer = FileInformationSerializer(file_info)
                return Response(serializer.data, status=201)

            except Exception as e:
                return Response({"message": str(e)}, status=500)
        else:
            return Response({"message": "File not found at specified path"}, status=400)

class get_file_information(APIView):
    def get(self, request, file_id):
        try:
            file_info = FileInformation.objects.get(id=file_id)
            serializer = FileInformationSerializer(file_info)
            return Response(serializer.data, status=200)
        except FileInformation.DoesNotExist:
            return Response({"message": "File not found"}, status=404)

class SensorDataView(APIView):
    def get(self, request):
        try:
            # Read sensor_data.json file
            with open('D:\hackathon\hack_project\sensor_data\sensor_data.json') as file:
                data = json.load(file)
            # Save or update the data in the database (assuming one entry for simplicity)
            sensor_data, _ = SensorData.objects.get_or_create(data=data)
            sensor_data.data = data
            sensor_data.save()

            # Serialize and return the data
            serializer = SensorDataSerializer(sensor_data)
            return Response(serializer.data, status=200)

        except FileNotFoundError:
            return Response({"message": "File not found"}, status=404)