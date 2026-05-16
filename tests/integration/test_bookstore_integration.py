from backend.bookstore import BookStore
from backend.favorite_books import FavoriteBooks


def test_book_can_be_added_to_favorites():
    store = BookStore()
    favorites = FavoriteBooks()

    store.addBook("Veronica", "Salminen")

    book = store.books[0]

    favorites.add(book)

    assert len(favorites.favorites) == 1

# Testar att bookstore och favorebooks fungerar tillsammans i ett flöde
def test_book_can_be_favorited_and_stored():
    store = BookStore()
    favorites = FavoriteBooks()

    store.addBook("Veronica", "Salminen")
    store.toggleFavorite(0)

    book = store.books[0]

    if book["favorite"]:
        favorites.add(book)

    assert len(favorites.favorites) == 1