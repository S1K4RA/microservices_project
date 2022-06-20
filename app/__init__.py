from flask import Flask, render_template, redirect, request, session
from flask_session import Session

import redis
#Init Flask
app = Flask(__name__,template_folder="templates/")

app.secret_key = 'BAD_SECRET_KEY'

#Flask Session
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_USE_SIGNER'] = True
app.config["SESSION_TYPE"] = 'redis'
app.config['SESSION_REDIS'] = redis.from_url('redis://redis:6379')

# Create and initialize the Flask-Session object AFTER `app` has been configured
server_session = Session(app)


from app import routes
# from worker import tasks
