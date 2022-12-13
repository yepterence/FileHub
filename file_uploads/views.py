from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadedFileForm

from .models import UploadedFile


def upload_file(request):
    """Display form for file upload"""

    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            print(uploaded_file)
            form.save()
            return HttpResponseRedirect('')
    else:
        form = UploadedFileForm()
    return render(request, 'file_uploads/upload_files.html', {'form': form})
