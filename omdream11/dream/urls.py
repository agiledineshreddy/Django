# dream/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dream, name='dream'),
    path('intro/', views.dream, name='dream'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('bet/', views.bet, name='bet'),
  
]
