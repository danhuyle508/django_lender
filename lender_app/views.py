from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Book

@login_required
def book_list_view(request):
    books = get_list_or_404(Book)
    context ={
        'books': books,
    }
    return render(request, 'generic/book_list.html', context)

@login_required
def book_detail_view(request, pk=None):
    book = get_object_or_404(Book, id=pk)
    context = {
        'book': book,
    }
    return render(request, 'generic/book_detail.html', context)