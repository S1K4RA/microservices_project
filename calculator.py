import json

from http import cookies
from unittest import result
from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from werkzeug.wrappers import Response


class GatewayService:
    name = 'calculator_gateway'
    c_rpc = RpcProxy('calculator_service')
    # session_provider = SessionProvider()
    
    @http('GET', '/api/prime/<int:index>')
    def prime_service(self, request, index):
        prime = self.c_rpc.prime_service(index)
        return json.dumps({"result": prime})
    
    @http('GET', '/api/prime/palindrome/<int:index>')
    def prime_palindrome_service(self, request, index):
        palin = self.c_rpc.prime_palindrome_service(index)
        return json.dumps({"result": palin})
    
    