from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
    # Retrieve unique cuisines from the database for the dropdown
    cuisines = Restaurant.objects.order_by().values_list('cuisine', flat=True).distinct()
    selected_cuisine = request.GET.get('cuisine')

    if selected_cuisine:
        # Filter the restaurants by the selected cuisine
        restaurants = Restaurant.objects.filter(cuisine=selected_cuisine).order_by('name')
    else:
        # Show all restaurants if no specific cuisine is selected
        restaurants = Restaurant.objects.all().order_by('name')

    context = {
        'restaurants': restaurants,
        'cuisines': cuisines,
        'selected_cuisine': selected_cuisine
    }
    return render(request, 'restaurants/restaurant_list.html', context)
