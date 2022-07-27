Feature: Items
  Make requests to items endpoint

  Scenario: Get many items
    Given the test-bees url
    When make a request to get all items
    Then the status_code is "200"
    And a list of valid items is returned

  Scenario: Create item
    Given the test-bees url
    And a valid item
    When make a request to post a valid item
    Then the status_code is "201"