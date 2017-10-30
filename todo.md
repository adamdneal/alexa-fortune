## Notes/resources
- https://developer.amazon.com/docs/custom-skills/steps-to-build-a-custom-skill.html
- https://developer.amazon.com/docs/ask-overviews/understanding-how-users-interact-with-skills.html
- https://developer.amazon.com/docs/custom-skills/use-the-skill-builder-beta-to-define-intents-slots-and-dialogs.html

## Todo
- [x] write interaction model
  - [x] needs unique invocation name ("fortune" is probably taken)
- [x] write py to parse fortune file
  - [x] may import to db/dynamo db
  - [ ] use http://boto3.readthedocs.io/en/latest/guide/dynamodb.html#batch-writing
  - [x] ** fix multi-line quote reading **
  - [x] dynamo dones't have built in support for random access. quickest way is to use DescribeTable call (up to 6 hours stale though)
  - [ ] uses strfile format for quicker random access: https://linux.die.net/man/1/strfile
- [x] write py for skill (started sample)
- [ ] ** add author param (slot) **
