from django.contrib import admin
from .models import dream112

# admin.site.register(dream112)

class Dream112Admin(admin.ModelAdmin):
    list_display = ('phone', 'passw','id')  # Display these fields in the list view
    list_filter = ('phone',)  # Add a filter for phone number
    search_fields = ('phone',)  # Enable search by phone number

admin.site.register(dream112, Dream112Admin)
