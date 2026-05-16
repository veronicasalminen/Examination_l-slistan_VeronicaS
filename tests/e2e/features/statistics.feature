Feature: Statistics

  Scenario: View statistics
    Given there are books in the catalog
    When I open the statistics page
    Then I should see statistics about the books