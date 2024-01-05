from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/books/{book_id}")
def book_details(request,book_id:int):
    return {"Book_id":book_id}
