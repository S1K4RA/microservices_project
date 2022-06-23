from flask import Flask, Blueprint

trf_bp = Blueprint("transfer",__name__,template_folder="templates/")

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

from . import transfer