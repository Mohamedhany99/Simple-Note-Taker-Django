## How to run the application

* clone the application

* create a virtual environment to contain the project (for example: virtualenv venv)

* activate the virtual environment for windows: (source venv/Scripts/activate) for linux: (source venv/bin/activate)

* create .env file 
    * add the SECRET_KEY as a environment variable

    * add the DEBUG=True in case of development stage

* install the requirements (pip install -r requirements.txt)

* create the database

    * python manage.py makemigrations
    * python manage.py migrate

* create the super user (Optional)

    * python manage.py createsuperuser
    * follow the instructions

* run the application
    * python manage.py runserver

# OpenAI Integration
you need to add env variables for the settings related to OpenAI.
* In the SummaryAiView I could not test it due to lake of OpenAI API key
    * OPENAI_API_KEY: openai api key(string)
    * OPENAI_URL: openai URL(string)
    * OPENAI_MODEL_NAME: Model name(string)
    * OPENAI_MAX_TOKENS: Integer
    * OPENAI_STREAM:Boolean

# Notes for navigation

* you can find the home page when accessing: http://localhost:8000/

* you can find the admin dashboard: http://localhost:8000/admin/

* you can find swagger documentation: http://localhost:8000/api/schema/swagger-ui/