class CatalogPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("http://localhost:3000")

    def favorite_button(self):
        return self.page.locator("[data-testid='favorite-button']")