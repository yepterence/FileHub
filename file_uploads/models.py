import uuid

from django.db import models


def custom_path(instance, filename):
    """Custom path for storing files upon file upload."""
    return f'{instance.unique_identifier}/{filename}'


class UploadedFile(models.Model):
    """Model for storing session information, file destination path, and additional information from Upload request."""
    text = models.CharField(max_length=100, default='', blank=False)
    number = models.IntegerField(help_text="Stores an integer value")
    session_id = models.CharField(max_length=100, default='', blank=False)
    unique_identifier = models.UUIDField(default=uuid.uuid4 ,help_text="Used for uniquely named folders per session")
    file = models.FileField(upload_to=custom_path, help_text="Stores file path")
    time_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}: {self.file.name}"
