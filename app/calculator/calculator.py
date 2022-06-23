import time
import json

from . import simple_app, calculator_bp

#Services
@calculator_bp.route('/<int:index>', methods=['GET'])
def primeService(index):
    task = simple_app.send_task(calculator_bp.name+'.tasks.primeService', kwargs={'index': index})
    # task = simple_app.apply_async(app.name+'.tasks.primeService', kwargs={'n': n})
    time.sleep(3)
    result = simple_app.AsyncResult(task.id).result
    print (result)  
    return json.dumps({"result": result, "id": task.id})

@calculator_bp.route('/palindrome/<int:index>', methods=['GET'])
def primePalindromeService(index):
    task = simple_app.send_task(calculator_bp.name+'.tasks.primePalindromeService', kwargs={'index': index})
    # task = simple_app.apply_async(app.name+'.tasks.primeService', kwargs={'n': n})
    time.sleep(3)
    result = simple_app.AsyncResult(task.id).result
    print (result)  
    return json.dumps({"result": result, "id": task.id})