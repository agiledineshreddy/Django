from django.shortcuts import render

# Create your views here.
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def search_books(request):
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'books/search_results.html', {'books': books})
