from django.urls import path

from . import views

app_name = 'file_uploads'
urlpatterns = [
    path('upload/', views.upload_file, name='upload'),
]
