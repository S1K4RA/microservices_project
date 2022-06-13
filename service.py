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


from nameko.rpc import rpc

class CalculatorService:
    name = "calculator_service"
    
    @rpc
    def prime_service(self, index):
        result = historic(index)
        return result
        
    
    @rpc
    def prime_palindrome_service(self, index):
        result = palindrome_historic(index)
        return result
        