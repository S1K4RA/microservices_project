# microservices_project

Prime and Prime Palindrome
Access on http://127.0.0.1:5000/


Ver. 1 Guide
Dependencies (For Windows)
> pip install gevent
> pip install -U Celery
> pip install "celery[redis]"
> pip install Flask

Install Virtual Environtment
> py -3 -m venv venv

Activate venv
> venv\Scripts\activate

Initialize Flask
> set FLASK_APP=routes.py
> flask run

activate celery
> celery -A tasks worker --loglevel=info -P gevent

redis for celery
broker, backend : redis://localhost:6379/0



Ver.2 Guide
Docker and docker-compose supported

>> docker-compose build
>> docker-compose up


redis for celery
broker, backend : redis://redis:6379/0