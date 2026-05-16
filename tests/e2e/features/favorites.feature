Feature: Favorite books

  Scenario: Add a book to favorites
    Given a book exists in the catalog
    When I mark the book as favorite
    Then the book should be saved under my favorites


Feature: Remove favorite marking

  Scenario: Remove a book from favorites
    Given a book exists in my favorites
    When I remove the favorite mark
    Then the book should no longer exists under my favorites