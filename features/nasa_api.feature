Feature: NASA API Interaction

  Scenario Outline: Validate Astronomy Picture of the Day API for defined date
    Given I have the NASA API key
    When I query the API for "<date>"'s picture
    Then the HTTP status code is 200
    And the response should include keys "<keys>"
    And the "media_type" should be either "image" or "video"
    And the "date" in the response should match the requested date

  Examples:
    | date       | keys                                         |
    | yesterday  | title, explanation, url, media_type, date    |
    | 2024-10-13 | title, explanation, url, media_type, date    |
    | 2024-09-13 | title, explanation, url, media_type, date    |