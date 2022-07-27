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

  Scenario: Create deposit with items list
    Given the test-bees url
    And a valid deposit
    And a list of valid items
    When make a request to post a valid deposit with items
    Then the status_code is "201"
    And a valid deposit is returned
    And with a list of valid items