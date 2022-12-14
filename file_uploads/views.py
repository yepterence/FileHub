from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadedFileForm

from .models import UploadedFile

from utils import utils


def upload_file(request):
    """Display form for file upload and perform processing on file"""

    process_results = None
    if request.method == 'POST':

        session_expiration_time = 60 * 30  # 30-minute session expiry window
        request.session.set_expiry(session_expiration_time)
        current_session = str(request.session.session_key)

        session_qs = UploadedFile.objects.order_by('time_uploaded').reverse()
        previous_session = session_qs[0].session_id

        form = UploadedFileForm(request.POST, request.FILES)

        if current_session != previous_session:

            if form.is_valid():
                obj = form.save(commit=False)
                obj.session_id = current_session
                obj.save()
                # perform processing
                process_results = utils.run_file_processor("process.sh", obj.text, obj.number)
                return HttpResponseRedirect('')
        elif current_session == previous_session:
            # if same session, insert uuid over-ride in form
            unique_id = UploadedFile.objects.filter(session_id=previous_session)[0].unique_identifier
            if form.is_valid():
                obj = form.save(commit=False)
                obj.unique_identifier = unique_id
                obj.save()
                # perform processing
                process_results = utils.run_file_processor("process.sh", obj.text, obj.number)
                return HttpResponseRedirect('')
    else:
        form = UploadedFileForm()

    return render(request, 'file_uploads/upload_files.html', {'form': form, 'process': process_results})
