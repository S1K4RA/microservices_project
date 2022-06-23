from flask import Blueprint, render_template, redirect, request, session
from celery import Celery

simple_app = Celery('simple_worker', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

calculator_bp = Blueprint("calculator",__name__,template_folder="templates/",url_prefix='/api/prime')

from . import calculator