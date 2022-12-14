from importlib import import_module
from subprocess import Popen, PIPE, STDOUT

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadedFileForm

from .models import UploadedFile

from utils import utils


def upload_file(request):
    """Display form for file upload"""

    if request.method == 'POST':

        session_expiration_time = 60 * 30
        request.session.set_expiry(session_expiration_time)
        current_session = str(request.session.session_key)
        qs = UploadedFile.objects.order_by('time_uploaded').reverse()
        previous_session = qs[0].session_id
        form = UploadedFileForm(request.POST, request.FILES)
        if current_session != previous_session:

            if form.is_valid():
                obj = form.save(commit=False)
                obj.session_id = current_session
                obj.save()
                return HttpResponseRedirect('')
        elif current_session == previous_session:
            # if same session, insert uuid over-ride in form
            unique_id = UploadedFile.objects.filter(session_id=previous_session)[0].unique_identifier
            if form.is_valid():
                obj = form.save(commit=False)
                obj.unique_identifier = unique_id
                obj.save()
                return HttpResponseRedirect('')
    else:
        form = UploadedFileForm()
    return render(request, 'file_uploads/upload_files.html', {'form': form})
