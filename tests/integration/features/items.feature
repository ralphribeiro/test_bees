Feature: Items
  Make requests to items endpoint

  Scenario: Get many items
    Given the test-bees url
    When make a request to get all "items"
    Then the status_code is "200"
    And a list of valid items is returned

  Scenario: Create item
    Given the test-bees url
    And a "valid" item
    When make a request to post item
    And save the "item" id
    Then the status_code is "201"
    And a valid item is returned
    And make request to delete a item by id

  Scenario: Create invalid item
    Given the test-bees url
    And a "invalid" item
    When make a request to post item
    Then the status_code is "400"

  Scenario: Get item by id
    Given the test-bees url
    And a "valid" item
    When make a request to post item
    Then the status_code is "201"
    And a valid item is returned
    When save the "item" id
    And make a request to get item by "valid" id
    Then the status_code is "200"
    And a valid item is returned
    And make request to delete a item by id

  Scenario: Get item by invalid id
    Given the test-bees url
    When make a request to get item by "invalid" id
    Then the status_code is "404"

  Scenario: Update item with patch
    Given the test-bees url
    And a "valid" item
    When make a request to post item
    Then the status_code is "201"
    And a valid item is returned
    When save the "item" id
    And make request to update a item values with "patch"
    Then the status_code is "200"
    And a valid item is returned
    And item values has changed
    And make request to delete a item by id

  Scenario: Update item with put
    Given the test-bees url
    And a "valid" item
    When make a request to post item
    Then the status_code is "201"
    And a valid item is returned
    When save the "item" id
    And make request to update a item values with "put"
    Then the status_code is "200"
    And a valid item is returned
    And item values has changed
    And make request to delete a item by id

  Scenario: Update item with invalid id
    Given the test-bees url
    And save the "item" id
    When make request to update a item values with "put"
    Then the status_code is "404"

  Scenario: Delete item
    Given the test-bees url
    And a "valid" item
    When make a request to post item
    Then the status_code is "201"
    And a valid item is returned
    When save the "item" id
    And make request to delete a item by id
    Then the status_code is "204"

  Scenario: Delete item with invalid id
    Given the test-bees url
    And save the "item" id
    When make request to delete a item by id
    Then the status_code is "404"