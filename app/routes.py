import time
from flask import render_template, redirect, request, session
from app import app
from celery import Celery

simple_app = Celery('simple_worker', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

import json

if __name__ == "__main__":
    app.run(debug=True)


#Lobby
@app.route("/login", methods=["POST", "GET"])
def login():
    # if form is submited
    if request.method == "POST":
        # record the user name
        session["name"] = request.form.get("name")
        # redirect to the main page
        return redirect("/")
    return render_template("login.html")

@app.route("/")
def index():
  # check if the users exist or not
    if not session.get("name"):
        # if not there in the session then redirect to the login page
        return redirect("/login")
    return render_template('index.html')

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")



#Services
@app.route('/api/prime/<int:index>', methods=['GET'])
def primeService(index):
    task = simple_app.send_task(app.name+'.tasks.primeService', kwargs={'index': index})
    # task = simple_app.apply_async(app.name+'.tasks.primeService', kwargs={'n': n})
    app.logger.info(task.backend)
    time.sleep(3)
    result = simple_app.AsyncResult(task.id).result
    print (result)  
    return json.dumps({"result": result, "id": task.id})

@app.route('/api/prime/palindrome/<int:index>', methods=['GET'])
def primePalindromeService(index):
    task = simple_app.send_task(app.name+'.tasks.primePalindromeService', kwargs={'index': index})
    # task = simple_app.apply_async(app.name+'.tasks.primeService', kwargs={'n': n})
    app.logger.info(task.backend)
    time.sleep(3)
    result = simple_app.AsyncResult(task.id).result
    print (result)  
    return json.dumps({"result": result, "id": task.id})