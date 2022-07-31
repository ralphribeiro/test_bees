Feature: Items

  Context: has authenticated

    Scenario: Create a new deposit
      Given that it is on the "deposits" page
      When create one "deposit"
      Then "deposit" has created

    Scenario: Delete a deposit
      Given that it is on the "deposits" page
      And created one "deposit"
      When destroy the created "deposit"
      Then "deposit" has destroyed

    Scenario: Update a deposit
      Given that it is on the "deposits" page
      And created one "deposit"
      When update "deposit"
      Then "deposit" has updated