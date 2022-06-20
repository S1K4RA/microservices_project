# microservices_project

Prime and Prime Palindrome

Dependencies (For Windows)
> pip install gevent
> pip install -U Celery
> pip install "celery[librabbitmq,redis,auth,msgpack]"
> pip install Flask

Install Virtual Environtment
> py -3 -m venv venv

Activate venv
> venv\Scripts\activate

Initialize Flask
> set FLASK_APP=routes.py
> flask run

activate celery
> celery -A app.tasks worker --loglevel=info -P gevent

Access on http://127.0.0.1:5000/