# FileHub

This application allows the user to upload files and store them on the server. 

## Objectives
- Allow user to interact with application and upload file to server.
- Uploaded files must be added to a single UUID folder per session.
- A secondary process runs, processing text and number inputs. 
- Contents of the file, length of text are to be displayed on the front end to the user.

### Methodology
- Created backend for the application using Django and Python.
- Files were saved to a UUID folder server based on session using Django's Sessions and request built-in framework. 
- A bash program was included to perform processing after the user uploads the file. This was accomplished using Python's subprocess library.
- Information was presented to user using a combination of HTML5/BootstrapCSS. 

### How to Launch the Application
- Clone this repo to your local.
- In your terminal, Make a virtual environment. (python3 -m venv venv)
- Install requirements using pip. (pip install -r requirements.txt)
- Navigate into the FileHub folder where manage.py is present and deploy the server using runserver (python3 manage.py runserver)
- Access the website in your favorite browser. (localhost:8000/file_uploads/upload) 