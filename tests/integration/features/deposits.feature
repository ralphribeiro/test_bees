Feature: Deposits
  Make requests to deposits endpoint

  Scenario: Get many deposits
    Given the test-bees url
    When make a request to get all "deposits"
    Then the status_code is "200"
    And a list of valid deposits is returned

  Scenario: Create deposit
    Given the test-bees url
    And a "valid" deposit
    When make a request to post deposit
    Then the status_code is "201"
    And a valid deposit is returned
    And save the "deposit" id
    And make request to delete a deposit by id

  Scenario: Create invalid deposit
    Given the test-bees url
    And a "invalid" deposit
    When make a request to post deposit
    Then the status_code is "400"

  Scenario: Get deposit by id
    Given the test-bees url
    And a "valid" deposit
    When make a request to post deposit
    Then the status_code is "201"
    And a valid deposit is returned
    When save the "deposit" id
    And make a request to get deposit by "valid" id
    Then the status_code is "200"
    And a valid deposit is returned
    And make request to delete a deposit by id

  Scenario: Get deposit by invalid id
    Given the test-bees url
    When make a request to get deposit by "invalid" id
    Then the status_code is "404"

  Scenario: Update deposit with patch
    Given the test-bees url
    And a "valid" deposit
    When make a request to post deposit
    Then the status_code is "201"
    And a valid deposit is returned
    When save the "deposit" id
    And make request to update a deposit values with "patch"
    Then the status_code is "200"
    And a valid deposit is returned
    And deposit values has changed
    And make request to delete a deposit by id

  Scenario: Update deposit with put
    Given the test-bees url
    And a "valid" deposit
    When make a request to post deposit
    Then the status_code is "201"
    And a valid deposit is returned
    When save the "deposit" id
    And make request to update a deposit values with "put"
    Then the status_code is "200"
    And a valid deposit is returned
    And deposit values has changed
    And make request to delete a deposit by id

  Scenario: Update deposit with invalid id
    Given the test-bees url
    And save the "deposit" id
    When make request to update a deposit values with "put"
    Then the status_code is "404"

  Scenario: Delete deposit
    Given the test-bees url
    And a "valid" deposit
    When make a request to post deposit
    Then the status_code is "201"
    And a valid deposit is returned
    When save the "deposit" id
    And make request to delete a deposit by id
    Then the status_code is "204"

  Scenario: Delete deposit with invalid id
    Given the test-bees url
    And save the "deposit" id
    When make request to delete a deposit by id
    Then the status_code is "404"