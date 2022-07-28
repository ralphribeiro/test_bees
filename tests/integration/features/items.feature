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
    And save the item id
    Then the status_code is "201"
    And a valid item is returned
    And make request to delete a item by id

  Scenario: Get item by id
    Given the test-bees url
    And a valid item
    When make a request to post a valid item
    Then the status_code is "201"
    And a valid item is returned
    When save the item id
    And make a request to get item by id
    Then the status_code is "200"
    And a valid item is returned
    And make request to delete a item by id

  Scenario: Update item with patch
    Given the test-bees url
    And a valid item
    When make a request to post a valid item
    Then the status_code is "201"
    And a valid item is returned
    When save the item id
    And make request to update a item values with "patch"
    Then the status_code is "200"
    And a valid item is returned
    And item values has changed
    And make request to delete a item by id

  Scenario: Update item with put
    Given the test-bees url
    And a valid item
    When make a request to post a valid item
    Then the status_code is "201"
    And a valid item is returned
    When save the item id
    And make request to update a item values with "put"
    Then the status_code is "200"
    And a valid item is returned
    And item values has changed
    And make request to delete a item by id

  Scenario: Delete item
    Given the test-bees url
    And a valid item
    When make a request to post a valid item
    Then the status_code is "201"
    And a valid item is returned
    When save the item id
    And make request to delete a item by id
    Then the status_code is "204"