
from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
# Create your views here.
class BookListview(ListView):
    

    template_name = 'bmi/book_list.html'
    model = Book