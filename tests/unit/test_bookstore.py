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