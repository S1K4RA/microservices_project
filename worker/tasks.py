import time
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

celery = Celery("app", 
            broker='redis://redis:6379/0',
            backend='redis://redis:6379/0',
            include=['tasks']
            )

def prime(i, primes):
        for prime in primes:
            if not (i == prime or i % prime):
                return False
        primes.append(i)
        return i

def historic(n):
    n += 1
    primes = list([])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes[-1]
        i += 1

def palindrome_historic(n):
    n += 1
    primes = list([])
    plndrm = list([])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            y = True
            if(str(i) == str(i)[::-1]):
                if (i>=2):
                    for a in range(2,i):
                        if(i%a==0):
                            y = False
                            break
                    if y:
                        plndrm.append(i)
                        p += 1
            if p == n:
                return plndrm[-1]
        i += 1

@celery.task(name='calculator.tasks.primeService')
def primeService(index):
    print("Task loaded")
    logger.info('Requested.Task Started')
    result = historic(index)
    logger.info('Task Completed')
    return result;
    
@celery.task(name='calculator.tasks.primePalindromeService')
def primePalindromeService(index):
    print("Task loaded")
    logger.info('Requested.Task Started')
    result = palindrome_historic(index)
    logger.info('Task Completed')
    return result;
    