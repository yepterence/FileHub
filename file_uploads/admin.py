from django.contrib import admin
from .models import UploadedFile


# Register your models here.

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('text', 'number', 'unique_identifier', 'file')

    search_fields = ('file', )


admin.site.register(UploadedFile, UploadedFileAdmin)
