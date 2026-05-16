from backend.bookstore import BookStore


def test_add_book():
    store = BookStore()

    store.addBook("Veronica", "Salminen")

    assert len(store.books) == 1