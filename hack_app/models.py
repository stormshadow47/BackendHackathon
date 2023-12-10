from django.db import models

class FileInformation(models.Model):
    filename = models.CharField(max_length=255)
    s3_url = models.URLField()
    upload_date = models.DateTimeField(auto_now_add=True)


class SensorData(models.Model):
    data = models.JSONField(null=True)  # Field to store the JSON data from sensor_data.json

