Feature: The Gate understands the slot names the model writes
  The envelope brief prints "- retention offer (KB11): OFFER", and the model copies that
  label back verbatim. The Gate canonicalises slot names before matching them against the
  catalogue, so a valid grant sentence is never lost and an email never escalates only
  because the model kept the KB reference. A name that still doesn't match after
  canonicalisation means the model tried to grant something outside the catalogue: a
  person sees it.

  Scenario Outline: A slot name that canonicalises is filled once
    Given customer <customer> writes "<message>"
    When the model returns the slots "<slots>"
    Then the reply contains "<sentence>"
    And the reply has <n> grant sentences
    And the Gate escalates with "<sources>"

    Examples:
      | customer | message                                                      | slots                                    | sentence                                          | n | sources                                        |
      | AC1009   | Please close the connection, we're vacating the house.       | retention offer (KB11)                   | 50% off your Pro plan for one month (KB11)        | 1 | none                                           |
      | AC1005   | Please waive the ₹100 late fee.                              | Late fee waiver                          | waived your ₹100 late fee (KB02)                  | 1 | none                                           |
      | AC1036   | I think I was charged twice this month.                      | double payment refund (KB04)             | refunded within                                   | 1 | none                                           |
      | AC1002   | I think I was charged twice this month.                      | double payment refund (KB04)             | a customer representative will call you           | 0 | gate:disallowed_offer:double payment refund    |
      | AC1009   | Please close the connection, we're vacating the house.       | retention offer, retention offer (KB11)  | 50% off your Pro plan for one month (KB11)        | 1 | none                                           |
      | AC1009   | Please close the connection, we're vacating the house.       | free month                               | a customer representative will call you           | 0 | gate:unknown_slot                              |
