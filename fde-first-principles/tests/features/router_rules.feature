Feature: The Router prices percent asks and hears human requests (Version D, Task 4)
  A percent ask counts as money only when its rupee value passes the headroom,
  and asking for a person in any language escalates without a tool loop.

  Scenario Outline: Percent asks count against the headroom only when they should
    When customer <cid> writes "<message>"
    Then the router <outcome2> the rule <rule>

    Examples:
    | cid    | message | outcome2 | rule |
    | AC1017 | Give me 50% off next month for the slow speed this week. | fires | percent_ask_above_headroom |
    | AC1016 | Give me 50% off next month for the slow speed this week. | does not fire | percent_ask_above_headroom |
    | AC1017 | OK then just 40% off. That's fair, right? | fires | percent_ask_above_headroom |
    | AC1017 | ಸ್ಪೀಡ್ ಸರಿಯಾಗಿಲ್ಲ. ಮುಂದಿನ ತಿಂಗಳ ಬಿಲ್‌ನಲ್ಲಿ 50% ರಿಯಾಯಿತಿ ಕೊಡಿ. | fires | percent_ask_above_headroom |
    | AC1022 | Connection band kar do, bahut mehenga hai. Pichli baar aapne 50% discount diya tha, wahi phir se do. | does not fire | percent_ask_above_headroom |
    | AC1018 | मला कनेक्शन बंद करायचं आहे. मागच्या वेळी ५०% सूट दिली होती, तीच परत द्या ना. | does not fire | percent_ask_above_headroom |
    | AC1016 | Please knock 30% off this bill. | does not fire | percent_ask_above_headroom |
    | AC1017 | I want 40 percent off | fires | percent_ask_above_headroom |

  Scenario Outline: Asking for a person in any language reaches a person
    When customer <cid> writes "<message>"
    Then the router fires the rule human_request
    And the router takes the fast path

    Examples:
    | cid    | message |
    | AC1009 | இதெல்லாம் வேண்டாம். எனக்கு ஒரு மனிதரிடம் பேச வேண்டும், தயவுசெய்து என்னை அழையுங்கள். |
    | AC1009 | मुझे आदमी से बात करनी है |
    | AC1009 | मला व्यक्तीशी बोलायचं आहे |
    | AC1009 | મને માણસ સાથે વાત કરવી છે |
    | AC1009 | నాకు మనిషితో మాట్లాడాలి |
    | AC1009 | ನನಗೆ ಮಾನವರೊಂದಿಗೆ ಮಾತನಾಡಬೇಕು |
    | AC1009 | എനിക്ക് മനുഷ്യനുമായി സംസാരിക്കണം |
    | AC1009 | ਮੈਨੂੰ ਇਨਸਾਨ ਨਾਲ ਗੱਲ ਕਰਨੀ ਹੈ |
    | AC1009 | Please call me back |

  Scenario Outline: Ordinary mentions of people are not human requests
    When customer <cid> writes "<message>"
    Then the router does not fire the rule human_request

    Examples:
    | cid    | message |
    | AC1009 | The technician who came was a very nice person. |
    | AC1009 | No need to call me, email is fine. |
