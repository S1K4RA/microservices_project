import os
from werkzeug.utils import secure_filename
from flask import flash, request, redirect, url_for, render_template, send_from_directory, current_app

# from app import app

from . import cloud_bp, UPLOAD_FOLDER, ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@cloud_bp.route('/cloud/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.root_path,UPLOAD_FOLDER, filename))
            return '<span>File Succesfully Uploaded</span>'
    return render_template("upload.html")

@cloud_bp.route('/cloud/download/<name>')
def download_file(name):
    filename = secure_filename(name)
    return send_from_directory(os.path.join(current_app.root_path,UPLOAD_FOLDER), filename)
