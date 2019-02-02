from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your tests here.
def index(req):
    return HttpResponse('Some data will be posted here')

def sample (req, x):
    return HttpResponse('another sampke is here %s' %x)