Feature: The Gate checks the model's draft before any grant sentence is written (Version D, Task 5)
  The model may not grant money or claim an action was done: code writes grants, code
  performs actions. Declines, conditional rules and restated hand-offs promise nothing.

  Scenario Outline: Draft sentences that grant or claim are caught; honest ones are not
    Given customer AC1009 asked for money
    When the model drafts "<draft>"
    Then the draft check reports <detector>

    Examples:
    | draft | detector |
    | We will refund your ₹500 now. | draft_grant |
    | I have cancelled your plan as requested. | action_claim |
    | Your upgrade is now active. | action_claim |
    | I cannot waive the ₹100 late fee here. | none |
    | If the outage lasts more than 24 hours, one day's charge is credited automatically. | none |
    | About your ₹500 credit request: a representative will call you. | none |
    | I have passed your request to our team. | none |
