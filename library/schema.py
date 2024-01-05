from ninja import Schema,ModelSchema
from books.models import Author,Book

class AuthorSchema(ModelSchema):
    class Meta:
        model = Author
        fields = "__all__"

class BookSchema(ModelSchema):
    author:AuthorSchema
    class Meta:
        model = Book
        fields = "__all__"

class BookInSchema(Schema):
    id:int
    title : str
    description : str
    author_id : int
    isbn : str