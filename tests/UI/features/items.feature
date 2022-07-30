Feature: Items

  Scenario: Create a new item
    Given that it is on the "items" page
    When create one "item"
    Then "item" has created


  Scenario: Delete a item
    Given that it is on the "items" page
    And created one "item"
    When delete the created "item"
    Then "item" has deleted
