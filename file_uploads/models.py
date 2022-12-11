from django.db import models


class File(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    file = models.FileField(upload_to='files/')
    time_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number + '-' + self.name
