from django.contrib import admin
from .models import FileInformation

@admin.register(FileInformation)
class FileInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename', 's3_url', 'upload_date')
    search_fields = ('filename', 's3_url')