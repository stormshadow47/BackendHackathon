"""
URL configuration for hack_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hack_app.views import upload_to_s3, get_file_information,get_csrf_token,SensorDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('api/upload/', upload_to_s3.as_view(), name='upload_to_s3'),
    path('api/file/<int:file_id>/', get_file_information.as_view(), name='get_file_information'),
    path('api/get-sensor-data/', SensorDataView.as_view(), name='get_sensor_data'),
]