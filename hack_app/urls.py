from django.urls import path
from hack_app.views import upload_to_s3, get_file_information,get_csrf_token, SensorDataView

urlpatterns = [
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('upload/',upload_to_s3.as_view(), name='upload_to_s3'),
    path('file/<int:file_id>/', get_file_information.as_view(), name='get_file_information'),
    path('get-sensor-data/', SensorDataView.as_view(), name='get_sensor_data'),
]
