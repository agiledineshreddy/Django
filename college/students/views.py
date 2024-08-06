from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('home.html')
    context={'message':'hello ommmm'}
    return render(request,'home.html',context)
def add(request):
    try:
        val1=int(request.GET['num1'])
        val2=int(request.GET['num2'])
        res= val1 + val2
        return render(request,'add.html',{'result':res})
    except (KeyError, ValueError):
        # Handle missing parameters or non-integer values
        return HttpResponseBadRequest('Invalid parameters')