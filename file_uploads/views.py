from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from utils import file_handler


def index(request):
    return render(request, 'file_uploads/base.html')

def upload(request):
    if request.method=='POST':
        uploaded_file = request.FILES['file']
    return

def upload_file(request):
    """Display form for file upload"""
    form = UploadFileForm()
    return render(request, 'file_uploads/upload_files.html', {'form': form})

    # """Display file upload form"""
    # if request.method == 'POST':
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         file_handler(request.FILES['file'])
    #         return HttpResponseRedirect('your/success/url/')
    # else:
    #     form = UploadFileForm()
    # return render(request, 'upload.html', {'form': form})
