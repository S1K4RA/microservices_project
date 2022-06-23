from flask import Flask, Blueprint

cloud_bp = Blueprint("cloud",__name__,template_folder="templates/")

UPLOAD_FOLDER = 'static/cloud'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

from . import cloud