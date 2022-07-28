Feature: Inventories

  Scenario: Get all inventories
    Given the test-bees url
    When make a request to get all inventories
    Then the status_code is "200"
    And a list of valid inventories is returned

  Scenario: Create invetory with one item
  Scenario: Create inventory with many items
  Scenario: Create inventory without items
  Scenario: Create inventory without deposit
  Scenario: Create inventory without items and deposit
  Scenario: Get inventory by id
  Scenario: Update inventory with patch
  Scenario: Update inventory with put
  Scenario: Delete inventory