# FastAPI Steps
To create and activate virtual environment
-pip install virtualenv
-virtualenv {environmentname}
- First go to {environmentname}/Scripts the command is cd {environmentname}/Scripts
-Then enter command activate
-Then enter command cd .. twice to come back
Modules to Install
-pip install SQLAlchemy
-pip install fastapi “uvicorn[standard]”
To start the server the command is uvicorn application:app –reload
To stop the server press crtl+c
