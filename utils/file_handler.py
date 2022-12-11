from uuid import uuid4


def create_uuid_directory():
    """Creates a unique uuid named directory for session."""
    return


def handle_uploaded_file(f, d, f_name):
    """Takes file, file name and directory as destination input and writes file to specified destination."""
    file_name = d + '/' + f_name + '.txt'
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
