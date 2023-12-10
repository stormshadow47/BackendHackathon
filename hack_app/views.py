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


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

class upload_to_s3(APIView):
    def post(self, request):
        credentials_file = request.FILES.get('credentials')

        if credentials_file:
            try:
                # AWS S3 Configuration
                s3 = boto3.client('s3',
                                  aws_access_key_id='AKIAS7QSBBMPO4KVRB54',
                                  aws_secret_access_key='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',
                                  region_name='ap-south-1')

                # Bucket and Key (File Path) in S3
                bucket_name = 'prjctbckt'
                s3_file_path = credentials_file.name  # Just the file name without any folder
                
                # Uploading file to S3
                s3.upload_fileobj(credentials_file, bucket_name, s3_file_path)

                # Save information to your database
                s3_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_file_path}"
                file_info = FileInformation.objects.create(
                    filename=credentials_file.name,
                    s3_url=s3_url
                )

                # Serialize and return the file information
                serializer = FileInformationSerializer(file_info)
                return Response(serializer.data, status=201)

            except Exception as e:
                return Response({"message": str(e)}, status=500)

        return Response({"message": "No file provided"}, status=400)


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