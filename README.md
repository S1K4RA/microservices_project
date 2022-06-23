# microservices_project

**Simple Microservices Project Using Docker**
Default access on http://127.0.0.1:5000/

Libraries / Packages used:
Flask - https://flask.palletsprojects.com/en/2.1.x/
Celery - https://docs.celeryq.dev/en/stable/
Redis - https://redis.io/docs/

This microservices is also deployed on Docker using docker-compose
docker-compose - https://docs.docker.com/compose/

Image used :
MySQL - https://hub.docker.com/_/mysql
phpMyAdmin - https://hub.docker.com/r/phpmyadmin/phpmyadmin/

There are 3 simple microservices written here:
1. Student Storage
How to Access : /student
Page : 
> /login
> /logout
> /register
> /paper/upload - Upload File
> /paper/(name) - Look for paper based on filename
> /paper/download/(name) - Download paper based on filename

*Accepted Extensions : pdf

2. Simple Calculator
How to Access : /api
Page :
> /prime/(index) - result of prime n-th
> /prime/palindrome/(index) - result of prime palindrome n-th

3. Simple Cloud Storage
How to Access : /cloud
Page : 
> /upload/ - Upload File
> /download/(name) - Download File

*Accepted Extensions : txt, pdf, png, jpg, jpeg, gif

**Dependencies**

Python
<code>pip install gevent</code>
<code>pip install -U Celery</code>
<code>pip install "celery[redis]"</code>
<code>pip install Flask</code>

**Running Without Docker**
Warning : Might not work. you need to change a few line of codes.

Install Virtual Environtment
<code>py -3 -m venv venv</code>

Activate venv
<code>venv\Scripts\activate</code>

Initialize Flask
<code>set FLASK_APP=routes.py</code>
<code>flask run</code>

activate celery
<code>celery -A tasks worker --loglevel=info -P gevent</code>

*use gevent if on Windows. skip if using Linux

redis for celery
broker, backend : redis://localhost:6379/0

**Running With Docker**
<code>docker-compose build</code>
<code>docker-compose up</code>

redis for celery
broker, backend : redis://redis:6379/0


