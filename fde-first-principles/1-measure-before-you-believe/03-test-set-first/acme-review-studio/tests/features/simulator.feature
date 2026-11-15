Feature: Run a test case against a specific workflow version

  Scenario: A run records the version it ran
    Given version "studio-offline@1.0.0" is frozen
    When I run case "c19" against "studio-offline@1.0.0"
    Then the run's version id is the frozen version's id
    And the run's pins equal the version's pins

  Scenario: Changing the model mid-batch doesn't change the batch
    Given a batch of 10 cases is running against "studio-offline@1.0.0"
    When another session switches the working copy to Claude Code
    Then every run in the batch used the offline drafter

  Scenario: A held run resumes on the version it started with
    Given case "c07" is held for review on "studio-offline@1.0.0"
    And the working copy now uses the C3 drafter
    When I approve the held draft
    Then the run finishes on "studio-offline@1.0.0"

  Scenario: The simulator shows C3's tool calls, not step 4's prompt
    Given version "studio-c3@1.0.0" binds the C3 agent loop to step 5
    When I run case "c19" and open step 5
    Then I see one row per tool call with its result
    And no prompt inspector is shown for step 4

  Scenario: A multi-agent version shows each agent in its own swimlane
    Given version "team-c3@1.0.0" runs a triage, specialist and reviewer team on the C3 agent loop
    When I run case "c19" against "team-c3@1.0.0"
    Then I see one swimlane per agent, joined by handoffs in run order
    And the specialist's lane lists its tool calls
    And the run is graded like any other version
