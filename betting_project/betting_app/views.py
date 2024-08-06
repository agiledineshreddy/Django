

# Create your views here.
from django.shortcuts import render, redirect
from .models import Bet
from django.contrib.auth.decorators import login_required

def home(request):
    bets = Bet.objects.all()
    return render(request, 'home.html', {'bets': bets})

@login_required
def bets(request):
    user_bets = request.user.bets.all()
    return render(request, 'bets.html', {'bets': user_bets})

def my_profile(request):
    return render(request, 'myprofile.html')
