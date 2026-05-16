from backend.bookstore import BookStore

# Testar att lägga till bok
def test_add_book():
    store = BookStore()

    store.addBook("Veronica", "Salminen")

    assert len(store.books) == 1

# Testar att markera bok som favorit
def test_toggle_favorite():
    store = BookStore()

    store.addBook("Veronica", "Salminen")

    store.toggleFavorite(0)

    assert store.books[0]["favorite"] is True

# Testar att favorit kan slå av och på igen
def test_toggle_favorite_twice():
    store = BookStore()
    store.addBook("Veronica", "Salminen")

    store.toggleFavorite(0)
    store.toggleFavorite(0)

    assert store.books[0]["favorite"] is False

# Addera fler böcker
def test_multiple_books():
    store = BookStore()

    store.addBook("Mimmi", "Pigg")
    store.addBook("Musse", "Pigg")

    assert len(store.books) == 2