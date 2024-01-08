from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from books.models import Book
from .schema import BookSchema,BookInSchema,BookPatchSchema
from typing import List

api = NinjaAPI()
# Here the docs page title change
api.title = "Ninja Crud"

@api.get("/books/{book_id}",response=BookSchema)
def book_details(request,book_id:int):
    book = get_object_or_404(Book,id=book_id)
    return book

@api.get("/books",response=List[BookSchema])
def book_list(request):
    return Book.objects.all()

@api.post("/books",response=BookSchema)
def create_book(request,payload:BookInSchema):
    book = Book.objects.create(**payload.dict())
    return book

@api.delete("/books/{book_id}")
def delete_book(request,book_id:int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"success":True}

@api.patch("/books/{book_id}",response=BookSchema)
def edit_book(request,book_id:int,payload:BookPatchSchema):
    book = get_object_or_404(Book,id=book_id)
    for attr,value in payload.dict(exclude_unset=True).items():
        setattr(book,attr,value)
    book.save()
    return book