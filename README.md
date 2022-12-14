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
- Make a virtual environment and source it. ```python3 -m venv venv ; source venv/bin/activate```
- Install dependencies. ```pip install -r requirements.txt```
- Navigate into the FileHub folder where manage.py is present and deploy the server using runserver ```python3 manage.py runserver```
- Access the website in your favorite browser. ```http://localhost:8000/file_uploads/upload``` 

### How it works
- Access the website using the address above. 
- Fill out the form: ![filled-out.png](..%2FPictures%2Ffilled-out.png)
- Navigate to uploads folder in FileHub home directory. A single file will exist within a UUID labeled folder.