Feature: Inventories

  Scenario: Get all inventories
    Given the test-bees url
    When make a request to get all "inventories"
    Then the status_code is "200"
    And a list of valid inventories is returned

  Scenario: Create invetory
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
    And a "valid" item
    And make a request to post item
    And save the new "item" id
    And make request to update a inventory values with "patch"
    Then the status_code is "200"
    And make request to delete a inventory by id
    And make request to delete a deposit by id
    And make request to delete a item by id
    And make request to delete a new item by id

  Scenario: Update inventory with put
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
    And a "valid" item
    And make a request to post item
    And save the new "item" id
    And make request to update a inventory values with "put"
    Then the status_code is "200"
    And make request to delete a inventory by id
    And make request to delete a deposit by id
    And make request to delete a item by id
    And make request to delete a new item by id

  Scenario: Delete inventory
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
    When make request to delete a inventory by id
    Then the status_code is "204"
    And make request to delete a deposit by id
    And make request to delete a item by id

  Scenario: Get Deposit with items
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
    When make a request to get deposit by "valid" id
    Then the deposit has been update with items
    And make request to delete a inventory by id
    And make request to delete a deposit by id
    And make request to delete a item by id

  Scenario: Try to delete item associated with an inventory
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
    When make request to delete a item by id
    Then the status_code is "500"
    And make request to delete a inventory by id
    And make request to delete a deposit by id
    And make request to delete a item by id

  Scenario: Try to delete deposit associated with an inventory
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
    When make request to delete a deposit by id
    Then the status_code is "500"
    And make request to delete a inventory by id
    And make request to delete a deposit by id
    And make request to delete a item by id