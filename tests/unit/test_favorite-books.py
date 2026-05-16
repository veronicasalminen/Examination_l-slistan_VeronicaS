from backend.favorite_books import FavoriteBooks


def test_add_favorite():
    favorites = FavoriteBooks()

    book = {"Veronica": "Salminen"}

    favorites.add(book)

    assert len(favorites.favorites) == 1