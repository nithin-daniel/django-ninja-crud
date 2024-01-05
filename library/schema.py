from ninja import schema


class BookSchema(schema):
    id : int
    title : str
    author_id : int
    isbn : str