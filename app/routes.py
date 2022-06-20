import time
from app import app
from celery import Celery

simple_app = Celery('simple_worker', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

import json

# if __name__ == "__main__":
#     app.run(debug=True)

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