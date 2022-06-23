from fileinput import filename
from turtle import title
from flask import Blueprint, render_template, redirect, request, session, jsonify, current_app, url_for, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flaskext.mysql import MySQL
from . import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
import uuid, logging, os
import pymysql

#MySQL
mysql = MySQL(cursorclass=pymysql.cursors.DictCursor) 

def student_blueprint(conn):
    student_bp = Blueprint("student_storage",__name__,template_folder="templates/",url_prefix='/student')
    
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    @student_bp.route("/login", methods=["POST", "GET"])
    def login():
        if request.method == "POST":
            _email = request.form['email']
            _password = request.form['password']
            
            if _email and _password:
                cursor = conn.cursor()
                sql = "SELECT * FROM user WHERE email = '{}'".format(_email)
                cursor.execute(sql)
                rows = cursor.fetchone()
                if rows is None:
                    return '<span>Email Not Found</span>'
                else:
                    if check_password_hash(pwhash=rows['password'], password=_password):
                        session['key'] = uuid.uuid1()
                        session['name'] = rows['name']
                        session['nrp'] = rows['nrp']
                        return redirect("/student")
                    else:
                        return '<span>Password Incorrect</span>'                
            else:
                return '<span>Enter the required fields</span>'
        return render_template("login.html")

    @student_bp.route("/register", methods=["POST", "GET"])
    def register():
        if request.method == "POST":
            _name = request.form['name']
            _nrp = request.form['nrp']
            _email = request.form['email']
            _password = request.form['password']
            # current_app.logger.info(request.form['email'])
            
            if _email and _password and _name and _nrp:
                cursor = conn.cursor()
                sql = "SELECT * FROM user WHERE email = '{}'".format(_email)
                cursor.execute(sql)
                if cursor.rowcount > 0:
                    return '<span>Username Already Registered</span>'
                else:
                    _hashedpassword = generate_password_hash(_password)
                    sql = "INSERT INTO user VALUES ('{}', '{}', '{}', '{}')".format(_nrp,_name,_email,_hashedpassword)
                    try:
                        cursor.execute(sql)
                        conn.commit()
                    except Exception as e:
                        current_app.logger.info("Failed To Insert" + str(e))
                        
                    cursor.close()
                    return redirect("/student")    
            else:
                return '<span>Enter The Required Fields</span>'
            
        return render_template("register.html")

    @student_bp.route("/")
    def index():
        return render_template('index.html')

    @student_bp.route("/logout")
    def logout():
        session.pop('key', None)
        return redirect("/")
           
    @student_bp.route("/upload", methods=["POST", "GET"])
    def upload_file():
        if request.method == 'POST':
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
                _abs = request.form['abstract']
                _title = request.form['title']
                filename = secure_filename(file.filename)
                
                cursor = conn.cursor()
                sql = "INSERT INTO paper VALUES ('{}', '{}', '{}', '{}')".format(session['nrp'],_title,filename,_abs)
                try:
                    cursor.execute(sql)
                    conn.commit()
                except Exception as e:
                    current_app.logger.info("Failed To Insert" + str(e))
                cursor.close()
                    
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                return '<span>File Succesfully Uploaded. Owner : {} </span>'.format(session['nrp'])
                # return redirect(url_for('student_storage.download_file', name=filename))
        return render_template("upload.html")
    
    @student_bp.route('/paper/<name>', methods=["POST", "GET"])
    def find_paper(name):
        if request.method == 'POST':
            return redirect(url_for('student_storage.download_paper', name=name))
        cursor = conn.cursor()
        sql = "SELECT * FROM paper WHERE path = '{}'".format(name)
        cursor.execute(sql)
        if cursor.rowcount > 0:
            rows = cursor.fetchone()
            return render_template("paper.html",title= rows['title'], abstract=rows['abstract'], name=name )    
        return '<span>File Not Found</span>'
    
    @student_bp.route('/paper/download/<name>')
    def download_paper(name):
        filename = secure_filename(name)
        cursor = conn.cursor()
        sql = "SELECT * FROM paper WHERE path = '{}'".format(filename)
        cursor.execute(sql)
        if cursor.rowcount > 0:
            rows = cursor.fetchone()
            if rows['owner'] == session['nrp']:
                return send_from_directory(UPLOAD_FOLDER, filename)
            else:
                return '<span>Access Denied. Owner: {} </span>'.format(rows['owner'])
        return '<span>File Not Found </span>'
    
    return student_bp