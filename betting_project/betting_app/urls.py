from django.urls import path
from .views import home, bets, my_profile

urlpatterns = [
    path('', home, name='home'),
    path('bets/', bets, name='bets'),
    path('myprofile/', my_profile, name='myprofile'),
]
