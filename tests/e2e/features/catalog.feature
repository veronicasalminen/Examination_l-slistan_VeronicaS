Feature: Book catalog

  Scenario: See all the books in the catalog
    Given the book catalog contains books
    When I open the book catalog
    Then I should see a list of all books

