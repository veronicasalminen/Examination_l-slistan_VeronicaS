from backend.bookstore import BookStore
from backend.favorite_books import FavoriteBooks


def test_book_can_be_added_to_favorites():
    store = BookStore()
    favorites = FavoriteBooks()

    store.addBook("Veronica", "Salminen")

    book = store.books[0]

    favorites.add(book)

    assert len(favorites.favorites) == 1