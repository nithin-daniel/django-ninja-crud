from ninja import Schema


class BookSchema(Schema):
    id : int
    title : str
    author_id : int
    isbn : str

class BookInSchema(Schema):
    id:int
    title : str
    description : str
    author_id : int
    isbn : str