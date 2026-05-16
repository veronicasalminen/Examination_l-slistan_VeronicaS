Feature: Add books
  Scenario: Add a new book
    Given the book does not exist in the catalog
    When I add the book
    Then the book should be added in the catalog