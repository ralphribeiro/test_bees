Feature: Inventories

  Scenario: Get all inventories
    Given the test-bees url
    When make a request to get all "inventories"
    Then the status_code is "200"
    And a list of valid inventories is returned

  Scenario: Create invetory with one item
    Given the test-bees url
    And a "valid" item
    And make a request to post item
    And the status_code is "201"
    And save the "item" id
    And a "valid" deposit
    And make a request to post deposit
    And the status_code is "201"
    And save the "deposit" id
    When make a valid inventory payload
    And make a request to post inventory
    Then the status_code is "201"
    And save the "inventory" id
    And a valid inventory is returned
    And make request to delete a inventory by id
    And make request to delete a deposit by id
    And make request to delete a item by id

  Scenario: Create inventory without deposit
    Given the test-bees url
    And a "valid" deposit
    And make a request to post deposit
    And the status_code is "201"
    And save the "deposit" id
    When make a valid inventory payload
    And make a request to post inventory
    Then the status_code is "422"
    And make request to delete a deposit by id

  Scenario: Create inventory without item
    Given the test-bees url
    And a "valid" item
    And make a request to post item
    And the status_code is "201"
    And save the "item" id
    When make a valid inventory payload
    And make a request to post inventory
    Then the status_code is "422"
    And make request to delete a item by id

  Scenario: Create inventory without items and deposit
    Given the test-bees url
    When make a valid inventory payload
    And make a request to post inventory
    Then the status_code is "422"

  Scenario: Get inventory by id
    Given the test-bees url
    And a "valid" item
    And make a request to post item
    And the status_code is "201"
    And save the "item" id
    And a "valid" deposit
    And make a request to post deposit
    And the status_code is "201"
    And save the "deposit" id
    When make a valid inventory payload
    And make a request to post inventory
    Then the status_code is "201"
    When save the "inventory" id
    And make a request to get inventory by "valid" id
    Then the status_code is "200"
    And a valid inventory is returned
    And make request to delete a inventory by id
    And make request to delete a deposit by id
    And make request to delete a item by id
  
  Scenario: Update inventory with patch
  Scenario: Update inventory with put
  Scenario: Delete inventory
    

  Scenario: Get Deposit with items