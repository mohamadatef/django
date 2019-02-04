from django.shortcuts import render, redirect
from .models import Data
from django.template import loader
from .forms import dataForm
# Create your views here.
from django.http import HttpResponse
# Create your tests here.
def index(req):

    dataList = Data.objects.order_by('id').reverse()
    template = loader.get_template('data/index.html')
    context = {
        'dataList' : dataList
    }
    return render(req, 'data/index.html' , context)
   # return HttpResponse(template.render(context, req))
def sample (req, x):
    return HttpResponse('another sampke is here %s' %x)

def addData (req):
    if req.method == 'POST':
        form  = dataForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form  = dataForm()
        context = {
        'form' :  form
        }
    return  render(req, 'data/addData.html', context)




def editData (req, id):
    if req.method =='GET':
        form   = Data.objects.get(pk = id)
        context ={

            'data' : form 
        }
        return render(req, 'data/editData.html' , context)


    