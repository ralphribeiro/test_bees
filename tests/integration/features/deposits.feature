Feature: Deposits
  Make requests to deposits endpoint

  Scenario: Get many deposits
    Given the test-bees url
    When make a request to get all deposits
    Then the status_code is "200"
    And a list of valid deposits is returned

  Scenario: Create deposit
    Given the test-bees url
    And a valid deposit
    When make a request to post a valid deposit
    Then the status_code is "201"
    And a valid deposit is returned
    And save the deposit id
    And make request to delete a deposit by id

  Scenario: Get deposit by id
    Given the test-bees url
    And a valid deposit
    When make a request to post a valid deposit
    Then the status_code is "201"
    And a valid deposit is returned
    When save the deposit id
    And make a request to get deposit by id
    Then the status_code is "200"
    And a valid deposit is returned
    And make request to delete a deposit by id

  Scenario: Update deposit with patch
    Given the test-bees url
    And a valid deposit
    When make a request to post a valid deposit
    Then the status_code is "201"
    And a valid deposit is returned
    When save the deposit id
    And make request to update a deposit values with "patch"
    And save the deposit id
    Then the status_code is "200"
    And a valid deposit is returned
    And deposit values has changed
    And make request to delete a deposit by id

  Scenario: Update deposit with put
    Given the test-bees url
    And a valid deposit
    When make a request to post a valid deposit
    Then the status_code is "201"
    And a valid deposit is returned
    When save the deposit id
    And make request to update a deposit values with "put"
    Then the status_code is "200"
    And a valid deposit is returned
    And deposit values has changed
    And make request to delete a deposit by id

  Scenario: Delete deposit
    Given the test-bees url
    And a valid deposit
    When make a request to post a valid deposit
    Then the status_code is "201"
    And a valid deposit is returned
    When save the deposit id
    And make request to delete a deposit by id
    Then the status_code is "204"