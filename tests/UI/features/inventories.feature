Feature: Inventories

  Context: has authenticated

    Scenario: Create a new inventory
      Given that an item and a deposit were created
      And that it is on the "inventories" page
      When create one inventory
      Then "inventory" has created

    Scenario: Delete a inventory
      Given created one inventory
      When destroy the created "inventory"
      Then "inventory" has destroyed

    Scenario: Update a inventory
      Given created one inventory
      When update inventory
      Then "inventory" has updated