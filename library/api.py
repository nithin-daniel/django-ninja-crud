from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from books.models import Book

api = NinjaAPI()

@api.get("/books/{book_id}")
def book_details(request,book_id:int):
    book = get_object_or_404(Book,id=book_id)
    return {
        "id":book_id,
        "title":book.title,
        "author":book.author.name,
        "isbn":book.isbn
    }