import imp
from django.shortcuts import render

from django.http import HttpResponse

from .models import Book

def index(request):
    return HttpResponse("BLACKPINK comeback in August 2022!")

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_detail.html', {'book':book})


