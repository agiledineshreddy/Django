from django.urls import path
from .import views


urlpatterns = [
   
    path('index',views.home),
     path('about',views.about),
      path('contact',views.contact),
       path('projects',views.projects),
]