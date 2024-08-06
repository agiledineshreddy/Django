from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'ass2.html')