from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from players.models import playerget

# def player(request):
#   template = loader.get_template('first.html')
#   context = {
#     "firstname": "Linus",
#   }
#   return HttpResponse(template.render(context, request))


# def player(request):
  
#   context = {
#     "firstname": "Linus",
#   }
#   return render(request, 'first.html',context)

 
def player(request):
  player_list=playerget.objects.all()
  player_dict={'player_list':player_list}
  return render(request, 'first.html',context=player_dict)


def player_data(request):    
  player_list=playerget.objects.all()
  player_dict={'player_list':player_list}
  return render(request, 'player_data.html',context=player_dict)

def details(request,id):
  player_list=playerget.objects.get(id=id)
  player_dict={'player_list':player_list}
  return render(request, 'details.html',context=player_dict)
def main(request):
  return render(request,'main.html')