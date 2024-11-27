Feature: Google search text
  Scenario: test google search
    #noinspection CucumberUndefinedStep
    Given I am on google search Page
    #noinspection CucumberUndefinedStep
    When I type in text to search
    #noinspection CucumberUndefinedStep
    And I hit Search button
    #noinspection CucumberUndefinedStep
    Then I should be on the search result Page
