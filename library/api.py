from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from books.models import Book
from .schema import BookSchema
from typing import List

api = NinjaAPI()

@api.get("/books/{book_id}",response=BookSchema)
def book_details(request,book_id:int):
    book = get_object_or_404(Book,id=book_id)
    return book

@api.get("/books",response=List[BookSchema])
def book_list(request):
    return Book.objects.all()