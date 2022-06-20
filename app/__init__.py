from flask import Flask
from celery import Celery
app = Flask(__name__)


celery = Celery(app.name, 
            broker='redis://localhost:6379/0',
            backend='redis://localhost:6379/0',
            include=['app.tasks']
            )

from app import routes, tasks
