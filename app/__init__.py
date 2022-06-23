import json
from flask import Flask, render_template, redirect, session
from flask_session import Session
import redis


UPLOAD_FOLDER = 'static'

#Init Flask
app = Flask(__name__,template_folder="templates/")


if __name__ == "__main__":
    app.run(debug=True)

#Flask Session
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_USE_SIGNER'] = True
app.config["SESSION_TYPE"] = 'redis'
app.config['SESSION_REDIS'] = redis.from_url('redis://redis:6379')

app.secret_key = 'VERYSECRET'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'research_paper'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_PORT'] = 3306

#MySQL
from .student_storage.routes import mysql, student_blueprint
mysql.init_app(app) 
conn = mysql.connect()

#Blueprints
from .calculator import calculator_bp
from .cloud import cloud_bp
from .student_storage import routes

app.register_blueprint(calculator_bp)
app.register_blueprint(cloud_bp)
app.register_blueprint(student_blueprint(conn))

# Create and initialize the Flask-Session object AFTER `app` has been configured
Session(app)
app.logger.info(app.url_map)

#Lobby
@app.route("/")
def index():
    return redirect ("/student/login")


