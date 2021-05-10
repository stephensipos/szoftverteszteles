
Feature: Authentication

  Scenario: No order has been placed
    Given we are on the order page
    Then cart has no elements

  Scenario: Empty cart
    Given we are on the order page
    Then an empty cart warning is displayed

  Scenario: Cart is not empty
    Given we are on the order page
    Given an roder has been palced
    When we reload the page
    Then no empty cart warning is displayed