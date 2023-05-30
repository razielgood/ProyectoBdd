Feature: Search and Add Product to Cart

  Scenario: Search for a product and add it to the cart
    Given I am on the Adidas website
    When I close the cookies notification
    And I search for "balon"
    Then I should see the search results
    And I add a product to the cart

