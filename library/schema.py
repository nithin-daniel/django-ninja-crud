from ninja import Schema


class BookSchema(Schema):
    id : int
    title : str
    author_id : int
    isbn : str