
Feature: User Table Testing

#Scenario: Visit Google
#  Given I go to "http://www.google.com/"
#  When I fill in field with class "gsfi" with "testingbot"
#  Then I should see "testingbot.com" within 2 second

Scenario: Select user_id from user_mobile
  Given I select recordnumber from loancore.user_personal_basic_info
  Then I query refused list
  Then I save the sql result as
  | filename        | type |
  | refuse_list     | csv  |