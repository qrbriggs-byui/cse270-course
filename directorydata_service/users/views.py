from django.shortcuts import render
import time
import random

# Create your views here.
from django.http import HttpResponse

MAGIC_PASSWORD = "CSE270Rocks!"

headers = {
"Cross-Origin-Opener-Policy":"unsafe-none",
'Access-Control-Allow-Origin':'*',
'Access-Control-Allow-Headers':'Origin, X-Requested-With, Content-Type, Accept'
}

def index(request):        
    print(request.GET.get("password"))
    if (request.GET.get("password")==MAGIC_PASSWORD):
        return HttpResponse(headers=headers)
    else:
        return HttpResponse(status=401,headers=headers)