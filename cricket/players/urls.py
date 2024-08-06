from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('player/', views.player, name='player'),
    path('player_data/',views.player_data, name='player_data'),
    path('player/details/<int:id>',views.details,name='details'),
    path('player/details/player/',views.player,name='player')
]