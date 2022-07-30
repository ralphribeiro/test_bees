Feature: Items

  Context: has authenticated

    Scenario: Create a new item
      Given that it is on the "items" page
      When create one "item"
      Then "item" has created

    Scenario: Delete a item
      Given that it is on the "items" page
      And created one "item"
      When destroy the created "item"
      Then "item" has destroyed

    Scenario: Update a item
      Given that it is on the "items" page
      And created one "item"
      When update "item"
      Then "item" has updated