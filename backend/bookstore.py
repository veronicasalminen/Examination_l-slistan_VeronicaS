
class BookStore:

    def __init__(self):
        self.books = []

    def addBook(self, author, title):
        self.books.append({
            "author": author,
            "title": title,
            "favorite": False
        })

#Växlar favorit status mellan true och false
    def toggleFavorite(self, book_id):
        self.books[book_id]["favorite"] = not self.books[book_id]["favorite"]
